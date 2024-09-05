import json
import time

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from django.views.generic import FormView, UpdateView, ListView
from django.contrib.auth.models import User
import requests

from log_storage.logging_config import logger_error, logger_develop

from .forms.upload_file_form import UserUploadDocumentForm, ClientUploadDocumentForm
from .forms.users_form import UserRegistrationForm, ProfileRegistrationForm, UserEditForm, ProfileEditForm, \
    CustomAuthenticationForm
from .models import ClientPreData, UserProfile, UserDocument, ClientDocument, Dealership
from .services.access_control_service import AccessControlService
from .services.common_servive import convert_str_list, handle_logger
from .services.index_list_application_service import ApplicationService
from .services.kafka.kafka_service import KafkaProducerService
from .services.offer_services.create_update_offers_in_db_service import CreateUpdateOffersInDbService
from .services.offer_services.get_offers_by_status import GetByStatusOfferService
from .services.offer_services.manage_select_offers_service import SelectedOfferService
from .services.offer_services.show_selected_offers_to_card import ShowOfferService
from .services.questionnaire.client_extra_data_service import ClientExtraDataService
from .services.questionnaire.questionnaire_view_services import QuestionnairePostHandler, QuestionnaireGetHandler
from .services.questionnaire.send_to_bank_service import SendToBankService
from .services.questionnaire.continue_docs_service import ContinueDocsService
from .services.upload_document_service import DocumentService


class ChangeActiveDealershipView(LoginRequiredMixin, View):
    @staticmethod
    def post(request, *args, **kwargs):
        dealership_id = request.POST.get('active_dealership')
        if dealership_id:
            user_profile = request.user.userprofile
            try:
                dealership = user_profile.dealership_manager.get(id=dealership_id)
                user_profile.set_active_dealership(dealership)
            except Dealership.DoesNotExist as e:
                handle_logger(e, logger_error)
                return JsonResponse("Dealership does not exist.")

        return redirect(request.META.get('HTTP_REFERER', 'home'))


class ContinueDocsView(LoginRequiredMixin, View):
    """Перенаправление на страницу оформления заявки после одобрения"""

    @staticmethod
    def get(request, *args, **kwargs):
        client_id = request.GET.get('client_id')
        id_app_in_system = request.GET.get('id_app_in_system')

        service = ContinueDocsService()
        context = service.get_context_for_continue_fill(client_id=client_id,
                                                        id_app_in_system=id_app_in_system)

        return render(request, 'continue_docs.html', context)


class RequestOffersView(LoginRequiredMixin, ListView):
    """Формирование страницы с заявками"""

    template_name = 'requests.html'
    context_object_name = 'status_offers'

    def get_queryset(self):
        bank_offer_service = GetByStatusOfferService()
        client_id = self.kwargs['client_id']
        return bank_offer_service.get_offers_by_status(client_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_id'] = self.kwargs['client_id']
        context['offers_by_status'] = self.get_queryset()
        return context


class SendToBankView(LoginRequiredMixin, View):
    """Отправка заявки в банк"""
    topic = 'database'
    kafka_service = KafkaProducerService()
    bank_offer_service = SendToBankService()

    def post(self, request, *args, **kwargs):
        client_id = request.POST.get('client_id')
        selected_offers = request.POST.getlist('selected_offers')

        if selected_offers:
            data = self.bank_offer_service.prepare_selected_offer_data(client_id,
                                                                       selected_offers)
            self.kafka_service.send_to_kafka(data,
                                             self.topic,
                                             client_id)

        converted_elected_offers = convert_str_list(selected_offers)

        for _ in range(60):
            if self.bank_offer_service.check_if_saved(client_id, converted_elected_offers):
                return redirect(f'/credit/requests/{client_id}/')
            time.sleep(1)

        return handle_logger('Офферы не были сохранены за отведенное время.',
                             logger_error,
                             additional_info=f'Не сохраненные id - {converted_elected_offers}')


class LoadAllDataClientView(LoginRequiredMixin, View):
    """
    Загрузка форм доп. информации о клиенте
    """

    @staticmethod
    def get(request, pk):
        client = get_object_or_404(ClientPreData, pk=pk)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            service = ClientExtraDataService(client)
            context = service.get_client_context()
            html = render_to_string('questionnaire/all_data_client.html',
                                    context,
                                    request=request)
            return JsonResponse({'html': html})
        return HttpResponse(status=400)

    @staticmethod
    def post(request, pk):
        client = get_object_or_404(ClientPreData, id=pk)
        service = ClientExtraDataService(client)

        form_data = {key: request.POST.dict() for key in service.forms_map.keys()}
        forms = service.prepare_forms(form_data)

        ignore_required = request.POST.get('ignore_required', 'false') == 'true'
        if ignore_required:
            service.set_fields_not_required(forms)

        if all(form.is_valid() for form in forms.values()):
            service.save_forms(forms)
            return JsonResponse({'success': True})
        else:
            errors = {form.__class__.__name__: form.errors for form in forms.values()}
            return JsonResponse({'success': False, 'error': errors}, status=400)


class QuestionnaireView(LoginRequiredMixin, View):
    """Представление для обработки создания и редактирования заявки клиента."""

    template_name = 'questionnaire/car_form.html'

    def get(self, request, *args, **kwargs):
        client_id = kwargs.get('pk')
        id_app_in_system = request.GET.get('id_app_in_system')
        id_app_bank = request.GET.get('id_app_bank')
        get_handler = QuestionnaireGetHandler()
        user = request.user
        active_dealership = user.userprofile.get_active_dealership()
        dealership_name = active_dealership.name if active_dealership else None

        redirect, context = get_handler.handle(client_id,
                                               id_app_in_system,
                                               id_app_bank, user,
                                               dealership_name)
        if redirect:
            return redirect
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        client_id = request.POST.get('client_id')
        ignore_required = request.POST.get('ignore_required', 'false') == 'true'
        form_data = request.POST.dict()
        post_handler = QuestionnairePostHandler()
        result = post_handler.handle(client_id, form_data, ignore_required)

        if result.get('success'):
            return JsonResponse({'success': True})
        else:
            return render(request, self.template_name, result)


class ManageSelectOffersView(LoginRequiredMixin, View):
    """CRUD карточек выбранных оферов"""

    @staticmethod
    def get(request, *args, **kwargs):
        client_id = request.GET.get('client_id')
        if not client_id:
            return JsonResponse({'status': 'error', 'message': 'client_id is required'}, status=400)

        offers_data = SelectedOfferService.get_offers(client_id=client_id)
        return JsonResponse({'offers': offers_data})

    @staticmethod
    def post(request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            client_id = data.get('client_id')
            offer_id = data.get('offer_id')
            total_loan_amount = data.get('total_loan_amount')

            if not client_id or not offer_id:
                return JsonResponse({'status': 'error', 'message': 'client_id and offer_id are required'}, status=400)

            result = SelectedOfferService.create_or_update_offer(
                client_id=client_id,
                offer_id=offer_id,
                total_loan_amount=total_loan_amount
            )
            return JsonResponse(result)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': e}, status=400)

    @staticmethod
    def delete(request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            client_id = data.get('client_id')
            offer_id = data.get('offer_id')

            if not client_id or not offer_id:
                return JsonResponse({'status': 'error', 'message': 'client_id and offer_id are required'}, status=400)

            result = SelectedOfferService.delete_offer(client_id=client_id,
                                                       offer_id=offer_id)
            return JsonResponse(result)

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': e}, status=400)


class ShowSelectCardOfferView(LoginRequiredMixin, View):
    """Отрисовка выбираемых оферов в предварительных расчетах после нажатия Выбрать"""

    @staticmethod
    def get(request, offer_id):
        try:
            car_price = request.GET.get('car_price')
            initial_payment = request.GET.get('initial_payment')
            total_loan_amount = request.GET.get('total_loan_amount')

            context = ShowOfferService.get_offer_data(
                offer_id=offer_id,
                car_price=car_price,
                initial_payment=initial_payment,
                total_loan_amount=total_loan_amount
            )

            return render(request, 'questionnaire/card_offer.html', context)
        except Http404 as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


class CreateUpdateOffersInDbView(LoginRequiredMixin, View):
    """Отображение и создание в БД предложений партнеров"""

    @staticmethod
    def get(request, *args, **kwargs):
        client_id = request.GET.get('client_id')
        if not client_id:
            return JsonResponse({'error': 'client_id is required'}, status=400)

        offers_data = CreateUpdateOffersInDbService.get_client_offers(client_id=client_id)
        return JsonResponse({'offers': offers_data})

    @staticmethod
    def post(request):
        financing_term = request.POST.get('financing_term')
        client_id = request.POST.get('client_id')

        if not financing_term or not client_id:
            return JsonResponse({'error': 'Invalid parameters'}, status=400)

        offers_html = CreateUpdateOffersInDbService.create_client_offers(client_id=client_id,
                                                                         financing_term=financing_term)
        return JsonResponse(offers_html, safe=False)


class IndexView(LoginRequiredMixin, View):
    """Отображение всех созданных заявок"""

    per_page = 10

    def get(self, request):
        # Получение параметров из запроса
        ordering = request.GET.get('ordering', '-date_create_all_app')
        dealership_filter = request.GET.get('dealership', '')
        status_filter = request.GET.get('status', '')

        # Используем сервис для получения заявок с фильтрацией
        object_list = ApplicationService.get_applications(
            user=request.user,
            dealership_filter=dealership_filter,
            status_filter=status_filter,
            ordering=ordering
        )

        # Пагинация
        paginator = Paginator(object_list, self.per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Маппинг полей на лейблы
        field_labels = {
            'client': 'ФИО',
            'statuses': 'Статус',
            'type': 'Тип',
            'financing': 'Финансирование',
            'author': 'Автор',
            'dealership': 'Дилерский центр',
            'organization': 'Юридическое лицо',
            'date_create': 'Дата создания',
            'date_changes': 'Дата изменения',
        }

        # Отправляем данные в шаблон
        return render(request, 'index.html', {
            'applications': page_obj,
            'dealership_filter': dealership_filter,
            'status_filter': status_filter,
            'field_labels': field_labels
        })


class RegisterView(LoginRequiredMixin, FormView):
    """Регистрация нового менеджера"""

    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    second_form_class = ProfileRegistrationForm
    success_url = reverse_lazy('user_list')

    def get_context_data(self, **kwargs):
        logger_develop('get  work')

        context = super(RegisterView, self).get_context_data(**kwargs)
        if 'profile_form' not in context:
            context['profile_form'] = self.second_form_class(request=self.request)
        else:
            context['profile_form'] = context['profile_form']
        return context

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(data=request.POST)

        profile_form = self.second_form_class(data=request.POST, request=request)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if not profile.organization_manager:
                profile.organization_manager = request.user.userprofile.organization_manager
            if not profile.role_manager:
                profile.role_manager = 'Менеджер ДЦ'

            profile.save()
            profile_form.save_m2m()

            selected_dealership = profile_form.cleaned_data.get('dealership_manager').first()
            if selected_dealership:
                profile.set_active_dealership(selected_dealership)
                profile.save()

            return redirect(self.success_url)
        else:
            return self.form_invalid(user_form, profile_form)

    def form_invalid(self, form, profile_form=None):
        # Если один из форм невалиден, необходимо отобразить обе формы, чтобы пользователь видел ошибки в обеих формах
        context = self.get_context_data()
        if isinstance(form, UserRegistrationForm):
            context['user_form'] = form
            context['profile_form'] = self.second_form_class(self.request.POST, request=self.request)
        else:
            context['user_form'] = self.form_class(self.request.POST)
            context['profile_form'] = form
        return self.render_to_response(context)


class UserEditView(LoginRequiredMixin, UpdateView):
    """CRUD существующего менеджера"""

    model = User
    form_class = UserEditForm
    template_name = 'users/edit_user.html'
    success_url = reverse_lazy('user_list')

    def dispatch(self, request, *args, **kwargs):
        """Проверка прав доступа перед выполнением запроса"""
        user_instance = self.get_object()
        user_profile = request.user.userprofile

        # Используем сервис для проверки прав доступа
        if not AccessControlService.has_access(user_profile, user_instance):
            return self.permission_denied_response("У вас нет доступа для редактирования этого пользователя.")

        return super().dispatch(request, *args, **kwargs)

    def permission_denied_response(self, message):
        """Возвращает JSON-ответ при недостатке прав"""
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': message}, status=403)
        else:
            return JsonResponse({'success': False, 'error': message}, status=403)

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_id'] = self.kwargs['pk']
        user_instance = self.get_object()

        if self.request.POST:
            context['profile_form'] = ProfileEditForm(self.request.POST, instance=user_instance.userprofile,
                                                      request=self.request)
        else:
            context['profile_form'] = ProfileEditForm(instance=user_instance.userprofile, request=self.request)

        context['next'] = self.request.GET.get('next', self.request.POST.get('next', ''))
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        profile_form = context['profile_form']

        # Проверка на игнорирование обязательных полей
        ignore_required = self.request.POST.get('ignore_required', 'false') == 'true'
        if ignore_required and self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            for field in profile_form.fields.values():
                field.required = False

        if profile_form.is_valid():
            self.object = form.save()
            profile_form.save()
            profile_form.save_m2m()
            if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'redirect_url': self.get_success_url()})
            next_url = self.request.POST.get('next', self.get_success_url())
            return HttpResponseRedirect(next_url)
        else:
            if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': profile_form.errors}, status=400)
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': form.errors}, status=400)
        return super().form_invalid(form)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        success_url = self.get_success_url()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'redirect_url': success_url})
        return redirect(success_url)

    def get_success_url(self):
        next_url = self.request.GET.get('next', self.request.POST.get('next', ''))
        return next_url if next_url else super().get_success_url()


class UserListView(LoginRequiredMixin, View):
    """Вывод всех зарегистрированных менеджеров, доступных для этой компании"""

    per_page = 5

    def get(self, request):
        ordering = request.GET.get('ordering', 'username')
        user_profile = UserProfile.objects.get(user=request.user)
        user_organization = user_profile.organization_manager

        if request.user.is_superuser:
            object_list = User.objects.all().select_related('userprofile').order_by(ordering)
        else:
            object_list = User.objects.filter(userprofile__organization_manager=user_organization).select_related(
                'userprofile').order_by(ordering)

        paginator = Paginator(object_list, self.per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        field_labels = {
            'username': 'Username',
            'email': 'Email',
            'userprofile__first_name_manager': 'Имя',
            'userprofile__last_name_manager': 'Фамилия',
            'userprofile__middle_name_manager': 'Отчество',
            'userprofile__date_of_birth_manager': 'Дата рождения',
            'userprofile__phone_number_manager': 'Телефон',
            'userprofile__organization_manager': 'Организация',
            'userprofile__status_manager': 'Статус',
        }

        return render(request, 'users/users.html', {
            'users': page_obj,
            'field_labels': field_labels
        })


class BaseUploadDocumentView(LoginRequiredMixin, FormView):
    """Базовый класс загрузки документов для клиента и менеджера в облако"""
    doc_service = DocumentService()
    document_model = None
    client_user_field_name = None

    def get_client_user(self):
        raise NotImplementedError("NotImplementedError")

    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            context = self.get_context_data(**kwargs)

            documents = context.get('documents', [])

            documents = self.doc_service.generate_signed_urls(documents)
            context['documents'] = documents

            html_form = render_to_string(self.template_name, context, request=request)
            return JsonResponse({'html_form': html_form})
        else:
            return render(request, self.template_name, self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, request.FILES)
            if form.is_valid():
                client = self.get_client_user()
                result = self.doc_service.process_upload(form, self.document_model, self.client_user_field_name, client)

                if result.get('status') == 'success':
                    return JsonResponse(result)
                elif result.get('status') == 'invalid':
                    return self.form_invalid(result.get('form'))
                else:
                    return result
            return self.form_invalid(form)
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

    def delete(self, request, *args, **kwargs):
        try:
            document_id = json.loads(request.body).get('document_id')
            document_model = kwargs.get('document_model')
            response = self.doc_service.delete_document(document_model, document_id)

            return response
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


class UserUploadDocumentView(BaseUploadDocumentView):
    """Загрузка документов менеджера в облако"""

    form_class = UserUploadDocumentForm
    template_name = 'users/upload_document_user.html'
    document_model = UserDocument
    client_user_field_name = 'user'

    def get_client_user(self):
        return get_object_or_404(User, id=self.request.POST.get('user_id'))

    def get_context_data(self, **kwargs):
        user = get_object_or_404(User, id=self.kwargs.get('pk'))
        documents = self.document_model.objects.filter(user=user)
        form = self.form_class(initial={'user_id': user.id})
        context = {
            'documents': documents,
            'user_id': user.id,
            'form': form
        }
        return context

    def delete(self, request, *args, **kwargs):
        try:
            document_id = json.loads(request.body).get('document_id')
            response = self.doc_service.delete_document(self.document_model, document_id)
            return response
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


class UploadDocumentView(BaseUploadDocumentView):
    """Загрузка документов клиента в облако"""

    form_class = ClientUploadDocumentForm
    template_name = 'questionnaire/upload_document_client.html'
    document_model = ClientDocument
    client_user_field_name = 'client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'documents': self.document_model.objects.filter(client_id=self.kwargs.get('pk')),
            'client_id': self.kwargs.get('pk')
        })
        return context

    def get_client_user(self):
        return get_object_or_404(ClientPreData, id=self.request.POST.get('client_id'))

    def delete(self, request, *args, **kwargs):
        try:
            document_id = json.loads(request.body).get('document_id')
            response = self.doc_service.delete_document(self.document_model, document_id)
            return response
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


class CustomPasswordResetView(SuccessMessageMixin, PasswordResetView):
    """Восстановление пароля"""

    email_template_name = 'reset_pass/password_reset_email.html'
    subject_template_name = 'reset_pass/password_reset_subject.txt'
    success_message = "На ваш адрес электронной почты было отправлено письмо с инструкциями по сбросу пароля."
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(self.request, "Пользователь с указанным адресом электронной почты не найден.")
            return redirect('password_reset')  # Перенаправление обратно на страницу сброса пароля

        # Генерация токена и URL для сброса пароля
        context = {
            'email': email,
            'domain': self.request.META['HTTP_HOST'],
            'site_name': 'MySite',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': default_token_generator.make_token(user),
            'protocol': 'https' if self.request.is_secure() else 'http',
        }
        subject = render_to_string(self.subject_template_name, context)
        subject = ''.join(subject.splitlines())
        body = render_to_string(self.email_template_name, context)

        # Отправка email через Unisender API
        url = "https://api.unisender.com/ru/api/sendEmail?format=json"
        payload = {
            'api_key': settings.UNISENDER_API_KEY,
            'email': email,
            'sender_name': 'Motor Finance',
            'sender_email': settings.DEFAULT_FROM_EMAIL,
            'subject': subject,
            'body': body,
            'list_id': settings.UNISENDER_LIST_ID,
        }

        response = requests.post(url, data=payload)
        if response.status_code != 200:
            messages.error(self.request, f"Ошибка при отправке письма: {response.json()}")
        else:
            messages.success(self.request, self.success_message)
        # Переопределяем стандартный метод, возвращая успешный ответ
        return redirect(self.success_url)


class CustomLoginView(LoginView):
    """Авторизация пользователя"""
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:

            return self.form_invalid(form)


def dadata_search(query):
    url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address"
    api_key = settings.DADATA_SEARCH_API_KEY

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Token {api_key}"
    }
    data = {
        "query": query,
        "count": 10
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}


def get_address_suggestions(request):
    query = request.GET.get('query', '')
    result = dadata_search(query)
    return JsonResponse(result)
