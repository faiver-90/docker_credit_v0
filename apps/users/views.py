import json
import time

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.views import View

from apps.common_services.paginator_service import PaginationService
from apps.common_services.upload_document_service import BaseUploadDocumentView
from apps.users.forms.users_form import UserEditForm, ProfileEditForm, UserRegistrationForm, ProfileRegistrationForm, \
    CustomAuthenticationForm, UserUploadDocumentForm
from apps.users.models import UserDocument
from apps.users.services.reset_pass_service import PasswordResetService
from apps.users.services.user_list_view_service import UserViewListService
from log_storage.logging_config import logger_develop


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


class UserListView(LoginRequiredMixin, View):
    """Вывод всех зарегистрированных менеджеров, доступных для этой компании"""
    per_page = 5

    def get(self, request):
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


class UserEditView(LoginRequiredMixin, UpdateView):
    """CRUD существующего менеджера"""
    model = User
    form_class = UserEditForm
    template_name = 'users/edit_user.html'
    success_url = reverse_lazy('user_list')

    def dispatch(self, request, *args, **kwargs):
        """Проверка прав доступа перед выполнением запроса"""
        user_instance = self.get_object()
        user = request.user
        user_profile = user.userprofile

        # Используем сервис для проверки прав доступа
        from apps.questionnaire.services.access_control_service import AccessControlService

        if not AccessControlService.has_access(user_profile, user_instance, is_superuser=user.is_superuser):
            return self.permission_denied_response("У вас нет доступа для редактирования этого пользователя.")

        return super().dispatch(request, *args, **kwargs)

    def permission_denied_response(self, message):
        """Возвращает JSON-ответ при недостатке прав"""
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': message}, status=403,
                                json_dumps_params={'ensure_ascii': False})
        else:
            return JsonResponse({'success': False, 'error': message}, status=403,
                                json_dumps_params={'ensure_ascii': False})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['user_id'] = self.kwargs['pk']
        user_instance = get_object_or_404(User, pk=self.kwargs['pk'])

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


class CustomPasswordResetView(SuccessMessageMixin, PasswordResetView):
    """Восстановление пароля"""
    reset_pass_service = PasswordResetService()
    email_template_name = 'users/reset_pass/password_reset_email.html'
    subject_template_name = 'users/reset_pass/password_reset_subject.txt'
    success_message = "На ваш адрес электронной почты было отправлено письмо с инструкциями по сбросу пароля."
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        email = form.cleaned_data['email']

        # Вызов сервиса для отправки письма
        response = self.reset_pass_service.send_password_reset_email(
            user_email=email,
            domain=self.request.META['HTTP_HOST'],
            is_secure=self.request.is_secure(),
            subject_template_name=self.subject_template_name,
            email_template_name=self.email_template_name
        )

        # Обработка результата из сервиса
        if response['status'] == 'error':
            messages.error(self.request, response['message'])
            return redirect('password_reset')
        else:
            messages.success(self.request, self.success_message)
            return redirect(self.success_url)
