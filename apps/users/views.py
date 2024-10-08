import json
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views import View

from apps.core.common_services.access_control_service import AccessControlService
from apps.core.common_services.paginator_service import PaginationService
from apps.core.common_services.upload_document_service import BaseUploadDocumentView
from apps.core.common_services.event_sourcing_service import EventSourcingService
from apps.users.forms.users_form import UserEditForm, ProfileEditForm, UserRegistrationForm, ProfileRegistrationForm, \
    CustomAuthenticationForm, UserUploadDocumentForm
from apps.users.models import UserDocument
from apps.users.services.reset_pass_service import PasswordResetService
from apps.users.services.user_edit_service import UserEditService
from apps.users.services.user_list_view_service import UserViewListService
import logging

logger = logging.getLogger(__name__)


class UserListView(LoginRequiredMixin, View):
    """
    Представление для отображения всех зарегистрированных пользователей (менеджеров), доступных для текущей компании.
    """
    per_page = 5

    def get(self, request):
        """
        Обрабатывает GET-запрос для отображения списка пользователей с пагинацией и сортировкой.

        Args:
            request: HTTP-запрос.

        Returns:
            HTTP-ответ с рендерингом страницы списка пользователей.
        """
        ordering = request.GET.get('ordering', 'username')
        page_number = request.GET.get('page', 1)

        users = UserViewListService.get_filtered_users(user=request.user, ordering=ordering)

        page_obj = PaginationService.paginate(users, page_number=page_number, per_page=self.per_page)

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


class UserUploadDocumentView(BaseUploadDocumentView, LoginRequiredMixin):
    """
    Представление для загрузки документов пользователя в облако.
    """
    form_class = UserUploadDocumentForm
    template_name = 'users/upload_document_user.html'
    document_model = UserDocument
    client_user_field_name = 'user'

    def get_client_user(self):
        """
        Получает пользователя, к которому относится загружаемый документ.

        Returns:
            Экземпляр пользователя (User).
        """
        return get_object_or_404(User, id=self.request.POST.get('user_id'))

    def get_context_data(self, **kwargs):
        """
        Формирует контекст для рендеринга страницы загрузки документа.

        Args:
            **kwargs: Дополнительные параметры контекста.

        Returns:
            Контекст данных для шаблона.
        """
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
        """
        Обрабатывает DELETE-запрос для удаления документа пользователя.

        Args:
            request: HTTP-запрос.

        Returns:
            JsonResponse с результатом удаления документа.
        """
        try:
            document_id = json.loads(request.body).get('document_id')
            response = self.doc_service.delete_document(self.document_model, document_id)
            return response
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


class UserEditView(LoginRequiredMixin, UpdateView):
    """
    Представление для редактирования существующего пользователя.
    """
    model = User
    form_class = UserEditForm
    template_name = 'users/edit_user.html'
    success_url = reverse_lazy('user_list')

    event_sourcing_service = EventSourcingService()
    access_control_service = AccessControlService()
    user_edit_service = UserEditService()

    def dispatch(self, request, *args, **kwargs):
        """
        Проверяет права доступа пользователя перед выполнением запроса.

        Args:
            request: HTTP-запрос.

        Returns:
            HTTP-ответ или редирект в случае отсутствия прав.
        """
        user_instance = self.get_object()
        user = request.user
        user_profile = user.userprofile

        if not self.access_control_service.has_access(user_profile, user_instance, is_superuser=user.is_superuser):
            return self.permission_denied_response("У вас нет доступа для редактирования этого пользователя.")

        return super().dispatch(request, *args, **kwargs)

    @staticmethod
    def permission_denied_response(message):
        """
        Возвращает JSON-ответ при недостатке прав доступа.

        Args:
            message: Сообщение об ошибке.

        Returns:
            JsonResponse с сообщением об ошибке.
        """
        return JsonResponse({'success': False, 'error': message}, status=403, json_dumps_params={'ensure_ascii': False})

    def get_context_data(self, **kwargs):
        """
        Формирует контекст для отображения формы редактирования профиля пользователя.

        Args:
            **kwargs: Дополнительные параметры контекста.

        Returns:
            Контекст данных для шаблона.
        """
        context = super().get_context_data(**kwargs)
        user_instance = self.get_object()
        target_id = context['user_id'] = user_instance.id
        user = context['user'] = self.request.user

        if self.request.POST:
            profile_form = context['profile_form'] = ProfileEditForm(self.request.POST,
                                                                     instance=user_instance.userprofile,
                                                                     request=self.request)

            self.handle_event_sourcing(profile_form, user, target_id)
        else:
            context['profile_form'] = ProfileEditForm(instance=user_instance.userprofile, request=self.request)

        context['next'] = self.request.GET.get('next', self.request.POST.get('next', ''))

        return context

    def handle_event_sourcing(self, profile_form, user, user_id):
        user_instance = self.get_object()
        if self.request.method == 'POST':
            old_values, new_values = self.event_sourcing_service.compare_fields_forms([profile_form], user_instance)

            payload = {}
            if profile_form.is_valid():
                payload['target_id'] = user_id
                payload = self.event_sourcing_service.field_entry_to_payload(old_values, new_values, payload)
                payload = self.user_edit_service.add_dealership_to_payload(user_instance, profile_form, payload)

                # Запись ивента
                self.event_sourcing_service.record_event(user.id, 'user_updated', payload, user_id)

    def form_valid(self, form):
        """
        Обрабатывает сохранение формы при валидных данных.

        Args:
            form: Валидная форма редактирования.

        Returns:
            JsonResponse или редирект на success_url.
        """
        context = self.get_context_data()
        profile_form = context['profile_form']

        # Проверка на игнорирование обязательных полей
        ignore_required = self.request.POST.get('ignore_required', 'false') == 'true'
        if ignore_required and self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            for field in profile_form.fields.values():
                field.required = False

        if profile_form.is_valid():
            form.save()
            profile_form.save()
            profile_form.save_m2m()
            if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'redirect_url': self.get_success_url()})
            next_url = self.request.POST.get('next', self.get_success_url())
            return HttpResponseRedirect(next_url)
        else:
            return self.form_invalid(form)

    def form_invalid(self, form):
        """
        Обрабатывает невалидные данные формы.

        Args:
            form: Невалидная форма.

        Returns:
            JsonResponse с ошибками или рендер страницы с ошибками.
        """
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': form.errors}, status=400)
        return super().form_invalid(form)

    def delete(self, request, *args, **kwargs):
        """
        Обрабатывает удаление пользователя и создание события в системе событий.

        Args:
            request: HTTP-запрос.

        Returns:
            JsonResponse или редирект на success_url.
        """
        user = self.get_object()

        payload = {
            'user_id': user.id,
            'username': user.username,
            'date': datetime.now().isoformat()
        }

        self.event_sourcing_service.record_event(user.id, 'user_deleted', payload)
        user.delete()

        success_url = self.get_success_url()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'redirect_url': success_url})
        return redirect(success_url)

    def get_success_url(self):
        """
        Получает URL для редиректа после успешного сохранения/удаления.

        Returns:
            URL для редиректа.
        """
        next_url = self.request.GET.get('next', self.request.POST.get('next', ''))
        return next_url if next_url else super().get_success_url()


class RegisterView(LoginRequiredMixin, FormView):
    """
    Представление для регистрации нового пользователя (менеджера).
    """
    template_name = 'users/register.html'
    form_class = UserRegistrationForm
    second_form_class = ProfileRegistrationForm
    success_url = reverse_lazy('user_list')
    event_sourcing_service = EventSourcingService()

    def get_context_data(self, **kwargs):
        """
        Формирует контекст для рендеринга страницы регистрации пользователя.

        Args:
            **kwargs: Дополнительные параметры контекста.

        Returns:
            Контекст данных для шаблона.
        """
        context = super(RegisterView, self).get_context_data(**kwargs)
        if 'profile_form' not in context:
            context['profile_form'] = self.second_form_class(request=self.request)
        return context

    def post(self, request, *args, **kwargs):
        """
        Обрабатывает POST-запрос для регистрации нового пользователя.

        Args:
            request: HTTP-запрос.

        Returns:
            Редирект на success_url при успешной регистрации или рендер формы с ошибками.
        """
        user = request.user.id
        user_form = self.form_class(data=request.POST)
        profile_form = self.second_form_class(data=request.POST, request=request)

        if user_form.is_valid() and profile_form.is_valid():
            created_user = user_form.save(commit=False)
            created_user.save()
            profile = profile_form.save(commit=False)
            profile.user = created_user

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

            payload = {
                'username_manager': created_user.username,
                'email_manager': created_user.email,
                'role_manager': created_user.userprofile.role_manager,
                'organization_manager': created_user.userprofile.organization_manager,
                'status_manager': created_user.userprofile.status_manager,
                'date_joined': created_user.date_joined.isoformat()
            }
            self.event_sourcing_service.record_event(user, 'user_created', payload, created_user.id)

            return redirect(self.success_url)
        else:
            return self.form_invalid(user_form, profile_form)

    def form_invalid(self, form, profile_form=None):
        """
        Обрабатывает невалидные формы и возвращает ошибки для обеих форм.

        Args:
            form: Невалидная форма регистрации пользователя.
            profile_form: Невалидная форма профиля пользователя (опционально).

        Returns:
            Рендер страницы с отображением ошибок.
        """
        context = self.get_context_data()
        context['user_form'] = form
        context['profile_form'] = profile_form if profile_form else self.second_form_class(self.request.POST,
                                                                                           request=self.request)
        return self.render_to_response(context)


class CustomLoginView(LoginView):
    """
    Кастомизированное представление для авторизации пользователя.
    """
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'

    def post(self, request, *args, **kwargs):
        """
        Обрабатывает POST-запрос для авторизации пользователя.

        Args:
            request: HTTP-запрос.

        Returns:
            Редирект при успешной авторизации или рендер страницы с ошибками.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)


class CustomPasswordResetView(SuccessMessageMixin, PasswordResetView):
    """
    Представление для сброса пароля пользователя.
    """
    reset_pass_service = PasswordResetService()
    email_template_name = 'users/reset_pass/password_reset_email.html'
    subject_template_name = 'users/reset_pass/password_reset_subject.txt'
    success_message = "На ваш адрес электронной почты было отправлено письмо с инструкциями по сбросу пароля."
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        """
        Обрабатывает валидную форму для сброса пароля и отправляет письмо.

        Args:
            form: Валидная форма сброса пароля.

        Returns:
            Редирект на success_url при успешной отправке письма или отображение ошибки.
        """
        email = form.cleaned_data['email']

        # Вызов сервиса для отправки письма
        response = self.reset_pass_service.send_password_reset_email(
            user_email=email,
            domain=self.request.META['HTTP_HOST'],
            is_secure=self.request.is_secure(),
            subject_template_name=self.subject_template_name,
            email_template_name=self.email_template_name
        )

        if response['status'] == 'error':
            messages.error(self.request, response['message'])
            return redirect('password_reset')
        messages.success(self.request, self.success_message)
        return redirect(self.success_url)
