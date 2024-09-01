import json
import logging
import time

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from django.views.generic import FormView, UpdateView, ListView
from django.contrib.auth.models import User
import requests
from .forms.car_application_form import CarInfoForm, DocumentAutoForm, ExtraForm, PreDataClientForm, \
    FinancingConditionsForm
from .forms.upload_file_form import UserUploadDocumentForm, ClientUploadDocumentForm
from .forms.users_form import UserRegistrationForm, ProfileRegistrationForm, UserEditForm, ProfileEditForm, \
    CustomAuthenticationForm
from .models import ClientPreData, SelectedClientOffer, AllApplications, ClientExtraInsurance, \
    ClientFinancingCondition, \
    ClientCarInfo, AutoSaleDocument, Offers, ClientOffer, UserProfile, UserDocument, ClientDocument, Dealership
from .services.common_servive import convert_str_list, handle_logger
from .services.kafka.kafka_service import KafkaProducerService
from .services.questionnaire.questionnaire_service import ClientExtraDataService
from .services.questionnaire.bank_offer_service import BankOfferService
from .services.upload_document_service import DocumentService

logger_debug = logging.getLogger('debug').debug
logger_info = logging.getLogger('info').info
logger_error = logging.getLogger('error').error


@login_required
def change_active_dealership(request):
    if request.method == 'POST':
        dealership_id = request.POST.get('active_dealership')
        if dealership_id:
            user_profile = request.user.userprofile
            try:
                dealership = user_profile.dealership_manager.get(id=dealership_id)
                user_profile.set_active_dealership(dealership)
            except Dealership.DoesNotExist as e:
                logger_error(e)
    return redirect(request.META.get('HTTP_REFERER', 'home'))


class ContinueDocsView(LoginRequiredMixin, View):
    """Перенаправление на страницу оформления заявки после одобрения"""

    def get(self, request, *args, **kwargs):
        client_id = request.GET.get('client_id')
        id_app_in_system = request.GET.get('id_app_in_system')
        client = get_object_or_404(ClientPreData, id=client_id)
        offer = SelectedClientOffer.objects.filter(client=client, id_app_in_system=id_app_in_system).first()
        car_form = CarInfoForm(instance=client.car_info.first(), request=request)
        document_form = DocumentAutoForm(instance=client.documents.first(), request=request)

        context = {
            'client_id': client_id,
            'offer': offer,
            'id_app_in_system': id_app_in_system,
            'car_form': car_form,
            'document': document_form,
            'hide_all_button': True
        }
        return render(request, 'continue_docs.html', context)


class RequestOffersView(LoginRequiredMixin, ListView):
    """Формирование страницы с заявками"""

    template_name = 'requests.html'
    context_object_name = 'status_offers'

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        offers = SelectedClientOffer.objects.filter(client_id=client_id)
        offers_data = {
            'Ошибка': [],
            'Ожидание решения': [],
            'Отказ': [],
            'Запрос доп информации': [],
            'Одобрение': []
        }
        for offer in offers:
            status = offer.status_select_offer
            if status:
                offer_data = render_to_string('questionnaire/card_offer.html', {
                    'offer': offer,
                    'client_id': client_id,
                    'hide_controls': True
                })
                offers_data[status].append(offer_data)
        return offers_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client_id'] = self.kwargs['client_id']
        context['offers_by_status'] = self.get_queryset()
        return context


class SendToBankView(LoginRequiredMixin, View):
    """Отправка заявки в банк"""
    topic = 'database'
    kafka_service = KafkaProducerService()
    bank_offer_service = BankOfferService()

    def post(self, request, *args, **kwargs):
        client_id = request.POST.get('client_id')
        selected_offers = request.POST.getlist('selected_offers')
        handle_logger(f'selected_offers 1, {selected_offers}', logger_info)
        if selected_offers:
            data = self.bank_offer_service.prepare_offer_data(client_id, selected_offers)
            self.kafka_service.send_to_kafka(data, self.topic, client_id)

        selected_offers = convert_str_list(selected_offers)
        handle_logger(f'selected_offers 2, {selected_offers}', logger_info)

        for _ in range(60):
            if self.bank_offer_service.check_if_saved(client_id, selected_offers):
                return redirect(f'/credit/requests/{client_id}/')
            time.sleep(1)

        return handle_logger('Офферы не были сохранены за отведенное время.',
                             logger_error,
                             additional_info=f'Не сохраненные id - {selected_offers}')


class LoadAllDataClientView(LoginRequiredMixin, View):
    """Загрузка форм доп. информации о клиенте"""

    def get(self, request, pk):
        client = get_object_or_404(ClientPreData, pk=pk)
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            service = ClientExtraDataService(client)
            context = service.get_client_context()
            html = render_to_string('questionnaire/all_data_client.html', context, request=request)
            return JsonResponse({'html': html})
        return HttpResponse(status=400)

    def post(self, request, pk):
        client = get_object_or_404(ClientPreData, id=pk)
        service = ClientExtraDataService(client, data=request.POST)
        forms = service.prepare_forms()

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
    """Создание новой заявки"""

    template_name = 'questionnaire/car_form.html'

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            client = get_object_or_404(ClientPreData, pk=kwargs['pk'])
            application = get_object_or_404(AllApplications, client=client)
            id_app_in_system = request.GET.get('id_app_in_system')
            id_app_bank = request.GET.get('id_app_bank')

            context = {
                'client_id': client.id,
                'application': application,
                'extra': ExtraForm(instance=client.extra_insurance.first()),
                'document': DocumentAutoForm(instance=client.documents.first()),
                'pre_data_client': PreDataClientForm(instance=client),
                'fin_cond': FinancingConditionsForm(instance=client.financing_conditions.first()),
                'car_form': CarInfoForm(instance=client.car_info.first()),
                'id_app_in_system': id_app_in_system,
                'id_app_bank': id_app_bank,
                'hide_controls': True,
            }

            # Проверяем, указан ли параметр id_app_in_system
            if id_app_in_system:
                select_offer = get_object_or_404(SelectedClientOffer, id_app_in_system=id_app_in_system)

                # Добавляем данные из SelectOffersClient в контекст
                offer_data = {
                    'offer': select_offer
                }
                context.update(offer_data)

        else:
            client, context = self.create_new_client(request)
            return HttpResponseRedirect(reverse('car_form', kwargs={'pk': client.pk}))

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        client_id = request.POST.get('client_id')
        client = get_object_or_404(ClientPreData, id=client_id)
        ignore_required = request.POST.get('ignore_required', 'false') == 'true'

        extra = ExtraForm(request.POST, instance=client.extra_insurance.first())
        document_form = DocumentAutoForm(request.POST, instance=client.documents.first())
        pre_data_client = PreDataClientForm(request.POST, instance=client)
        fin_cond = FinancingConditionsForm(request.POST, instance=client.financing_conditions.first())
        car_form = CarInfoForm(request.POST, instance=client.car_info.first())

        forms = [extra, document_form, pre_data_client, fin_cond, car_form]

        if ignore_required:
            for form in forms:
                for field in form.fields.values():
                    field.required = False

        if all([form.is_valid() for form in forms]):
            application = pre_data_client.save(commit=False)
            application.car_price_display = request.POST.get('car_price_display')
            application.additional_equipment_price_display = request.POST.get('additional_equipment_price_display')
            application.total_loan_amount = request.POST.get('total_loan_amount')
            application.save()
            fin_cond.save_or_update(client=client)
            car_form.save_or_update(client=client)
            document_form.save_or_update(client=client)
            extra.save_or_update(client=client)

            return JsonResponse({'success': True})
        else:
            context = {
                'client_id': client.id,
                'extra': extra,
                'document': document_form,
                'pre_data_client': pre_data_client,
                'fin_cond': fin_cond,
                'car_form': car_form
            }
            return render(request, self.template_name, context)

    @staticmethod
    def create_new_client(request):
        forms = {
            'client_temp_form': PreDataClientForm(),
            'car_form': CarInfoForm(),
            'document_form': DocumentAutoForm(),
            'financing_conditions_form': FinancingConditionsForm(),
            'extra_form': ExtraForm()
        }

        client = ClientPreData.objects.create(
            **{field_name: forms['client_temp_form'].fields[field_name].initial for field_name in
               forms['client_temp_form'].fields}
        )

        extra_insurance = ClientExtraInsurance.objects.create(
            client=client,
            **{field_name: forms['extra_form'].fields[field_name].initial for field_name in forms['extra_form'].fields}
        )

        financing_conditions = ClientFinancingCondition.objects.create(
            client=client,
            **{field_name: forms['financing_conditions_form'].fields[field_name].initial for field_name in
               forms['financing_conditions_form'].fields}
        )
        car_info = ClientCarInfo.objects.create(
            client=client,
            **{field_name: forms['car_form'].fields[field_name].initial for field_name in forms['car_form'].fields}
        )

        document = AutoSaleDocument.objects.create(
            client=client,
            **{field_name: forms['document_form'].fields[field_name].initial for field_name in
               forms['document_form'].fields}
        )
        active_dealership = request.user.userprofile.get_active_dealership()
        dealership_name = active_dealership.name if active_dealership else None

        AllApplications.objects.create(
            client=client,
            financing_conditions=financing_conditions,
            car_info=car_info,
            documents=document,
            extra_insurance=extra_insurance,
            status=' ',
            type_all_app=client.type_pre_client,
            financing=client.product_pre_client,
            manager=request.user.email,
            dealership_all_app=dealership_name,
            organization=request.user.userprofile.organization_manager,
        )

        context = {
            'extra': forms['extra_form'],
            'document': forms['document_form'],
            'client_temp': forms['client_temp_form'],
            'fin_cond': forms['financing_conditions_form'],
            'car_form': forms['car_form'],
            'client_id': client.id,
        }

        return client, context


class ManageSelectOffersView(LoginRequiredMixin, View):
    """CRUD карточек выбранных оферов"""

    def get(self, request, *args, **kwargs):
        client_id = request.GET.get('client_id')
        client = get_object_or_404(ClientPreData, id=client_id)
        selected_offers = SelectedClientOffer.objects.filter(client=client)
        offers_data = [self.render_offer(offer, client_id) for offer in selected_offers]
        return JsonResponse({'offers': offers_data})

    def render_offer(self, offer, client_id):
        context = {
            'offer': offer,
            'client_id': client_id,
            'hide_controls': False  # Удаление или показ кнопок выбрать, удалить на странице запросов
        }
        return render_to_string('questionnaire/card_offer.html', context)

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            client_id = data.get('client_id')
            offer_id = data.get('offer_id')
            total_loan_amount = data.get('total_loan_amount')

            if not client_id or not offer_id:
                return JsonResponse({'status': 'error', 'message': 'client_id and offer_id are required'}, status=400)

            client = get_object_or_404(ClientPreData, id=client_id)
            offer_details = get_object_or_404(Offers, id=offer_id)
            car_info = get_object_or_404(ClientCarInfo, client=client)
            financing_conditions = get_object_or_404(ClientFinancingCondition, client=client)
            select_offer, created = SelectedClientOffer.objects.update_or_create(
                client=client,
                offer_id=offer_id,
                defaults={
                    'car_price_display_select': car_info.car_price_car_info,
                    'initial_payment_select': financing_conditions.initial_payment,
                    'total_loan_amount_select': total_loan_amount,
                    'title_select': offer_details.title,
                    'term_select': offer_details.term,
                    'monthly_payment_select': offer_details.pay,
                    'stavka_select': offer_details.stavka,
                    'name_bank_select': offer_details.name_bank
                }
            )

            if created:
                select_offer.id_app_in_system = select_offer.id
                select_offer.save()

            return JsonResponse({'status': 'success'})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    @staticmethod
    def delete(request, *args, **kwargs):
        data = json.loads(request.body)
        offer_id = data.get('offer_id')
        client_id = data.get('client_id')
        if offer_id and client_id:
            client = get_object_or_404(ClientPreData, id=client_id)
            SelectedClientOffer.objects.filter(client=client, offer_id=offer_id).delete()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error'}, status=400)


#  Показыавть оферы при нажатии выбрать при превом запросе
class ShowSelectCardOfferView(LoginRequiredMixin, View):
    """Отрисовка выбираемых оферов в предварительных расчетах после нажатия Выбрать"""

    @staticmethod
    def get(request, offer_id):
        offer = get_object_or_404(Offers, id=offer_id)
        select_offer = SelectedClientOffer.objects.filter(offer_id=offer_id).first()

        if not select_offer:
            raise Http404("SelectOffersClient does not exist")

        # Передаем значения через GET параметры или используем значения из select_offer
        offer.car_price_display_select = request.GET.get('car_price', select_offer.car_price_display_select)
        offer.initial_payment_select = request.GET.get('initial_payment', select_offer.initial_payment_select)
        offer.total_loan_amount_select = request.GET.get('total_loan_amount', select_offer.total_loan_amount_select)
        offer.offer_id = offer_id

        offer.title_select = offer.title
        offer.name_bank_select = offer.name_bank
        offer.term_select = offer.term
        offer.stavka_select = offer.stavka
        offer.monthly_payment_select = offer.pay

        context = {
            'offer': offer,
            'client_id': select_offer.client.id,
            'hide_controls': False  # Пример, как можно управлять этим параметром
        }

        return render(request, 'questionnaire/card_offer.html', context)


class OffersView(LoginRequiredMixin, View):
    """Отображение и создание в БД предложений партнеров"""

    @staticmethod
    def get(request, *args, **kwargs):
        client_id = request.GET.get('client_id')
        client = get_object_or_404(ClientPreData, id=client_id)
        offers_client = ClientOffer.objects.filter(client=client)

        offers_data = []
        for offer in offers_client:
            offer_html = render_to_string('questionnaire/offer_item.html', {'offer': offer})
            offers_data.append(offer_html)

        return JsonResponse({'offers': offers_data})

    @staticmethod
    def post(request):
        financing_term = request.POST.get('financing_term')
        client_id = request.POST.get('client_id')

        if financing_term and client_id:
            offers = Offers.objects.filter(term=financing_term)
            client = ClientPreData.objects.get(pk=client_id)
            ClientOffer.objects.filter(client=client).delete()  # Удаляем предыдущие предложения

            offers_data = []
            for offer in offers:
                created_offer = ClientOffer.objects.create(
                    client=client,
                    offer_id=offer.id,
                    title_offer=offer.title,
                    name_bank_offer=offer.name_bank,
                    term_offer=offer.term,
                    stavka_offer=offer.stavka,
                    pay_offer=offer.pay
                )
                offers_data.append(created_offer)

            offers_html = []
            for offer in offers_data:
                offer_html = render_to_string('questionnaire/offer_item.html', {'offer': offer})
                offers_html.append(offer_html)

            return JsonResponse(offers_html, safe=False)

        return JsonResponse({'error': 'Invalid parameters'}, status=400)


class IndexView(LoginRequiredMixin, View):
    """Отображение всех созданных заявок"""

    per_page = 10

    def get(self, request):
        ordering = request.GET.get('ordering', '-date_create_all_app')
        user_profile = UserProfile.objects.get(user=request.user)
        user_organization = user_profile.organization_manager
        user_dealership = user_profile.get_active_dealership()
        user_role = user_profile.role_manager

        dealership_filter = request.GET.get('dealership', '')
        status_filter = request.GET.get('status', '')

        if request.user.is_superuser:
            object_list = AllApplications.objects.all().order_by(ordering)
        elif user_role == 'owner':
            object_list = AllApplications.objects.filter(
                organization=user_organization
            ).order_by(ordering)
        else:
            object_list = AllApplications.objects.filter(
                organization=user_organization,
                dealership_all_app=user_dealership if not dealership_filter else dealership_filter
            ).order_by(ordering)

        if status_filter:
            object_list = [app for app in object_list if
                           SelectedClientOffer.objects.filter(client=app.client,
                                                              status_select_offer=status_filter).exists()]

        # Добавление статусов к заявкам
        for application in object_list:
            offers = SelectedClientOffer.objects.filter(client=application.client).exclude(
                status_select_offer__isnull=True).exclude(status_select_offer__exact='')
            application.statuses = [{'status': offer.status_select_offer,
                                     'client_id': offer.client.id,
                                     'button_class': self.get_button_class(offer.status_select_offer)} for offer in
                                    offers]

        paginator = Paginator(object_list, self.per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

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
        return render(request, 'index.html', {
            'applications': page_obj,
            'dealership_filter': dealership_filter,
            'status_filter': status_filter,
            'field_labels': field_labels
        })

    @staticmethod
    def get_button_class(status):
        classes = {
            'Ошибка': 'btn btn-error',  # Оранжевый
            'Ожидание решения': 'btn btn-pending',  # Желтый
            'Отказ': 'btn btn-reject',  # Красный
            'Запрос доп информации': 'btn btn-request-info',  # Синий
            'Одобрение': 'btn btn-approve',  # Зеленый
            'Нет статуса': 'btn btn-light'  # Светлый
        }
        return classes.get(status, 'btn btn-light')  # Цвет по умолчанию


class RegisterView(LoginRequiredMixin, FormView):
    """Регистрация нового менеджера"""

    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    second_form_class = ProfileRegistrationForm
    success_url = reverse_lazy('user_list')

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        if 'profile_form' not in context:
            context['profile_form'] = self.second_form_class(request=self.request)
        else:
            context['profile_form'] = context['profile_form']
        return context

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST)
        profile_form = self.second_form_class(request.POST, request=request)

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
            profile_form.save_m2m()  # Save many-to-many relationships

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

        # Проверяем, если запрос содержит флаг игнорирования обязательных полей
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

        if request.user.username == 'admin':
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
    api_key = "43d1f880e47e4e9b7f45d470beb41cc070a14d04"
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
        response.raise_for_status()  # Это выбросит исключение для кода ответа != 200
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}


def get_address_suggestions(request):
    query = request.GET.get('query', '')
    result = dadata_search(query)
    return JsonResponse(result)
