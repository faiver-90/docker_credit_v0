from django.shortcuts import get_object_or_404

from credit_v0.forms.users_form import UserEditForm, ProfileEditForm
from credit_v0.models import User, UserProfile


class UserService:
    """Сервис для обработки операций с пользователем"""

    @staticmethod
    def get_user_object(user_id: int) -> User:
        """Получение объекта пользователя по ID"""
        return get_object_or_404(User, pk=user_id)

    @staticmethod
    def check_access(user_instance: User, current_user_id: int, current_user_role: str, organization_id: int) -> dict:
        """Проверка прав доступа на редактирование пользователя"""
        user_profile = user_instance.userprofile

        if current_user_role == 'admin':
            return {'can_edit': True}

        if current_user_role == 'Менеджер ДЦ' and user_instance.id != current_user_id:
            return {'error': "У вас нет доступа для редактирования этого пользователя."}

        if current_user_role == 'owner' and user_profile.organization_manager.id != organization_id:
            return {'error': "У вас нет доступа для редактирования пользователей из другой организации."}

        return {'can_edit': True}

    @staticmethod
    def validate_and_save_forms(user_instance: User, form_data: dict, ignore_required: bool, is_ajax: bool) -> dict:
        """Валидация и сохранение форм пользователя и профиля"""
        profile_form = ProfileEditForm(form_data, instance=user_instance.userprofile)
        user_form = UserEditForm(form_data, instance=user_instance)

        if ignore_required and is_ajax:
            for field in profile_form.fields.values():
                field.required = False

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            profile_form.save_m2m()
            return {'success': True, 'redirect_url': '/user_list/'}
        else:
            return {'success': False, 'errors': profile_form.errors}

    @staticmethod
    def delete_user(user_instance: User) -> dict:
        """Удаление пользователя"""
        user_instance.delete()
        return {'success': True, 'redirect_url': '/user_list/'}
