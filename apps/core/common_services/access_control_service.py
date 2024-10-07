import logging

logger = logging.getLogger(__name__)


class AccessControlService:
    """Сервис для проверки доступа на основе роли пользователя."""

    @staticmethod
    def has_access(user_profile, user_instance, **kwargs):
        """Проверка доступа на редактирование профиля пользователя."""
        is_superuser = kwargs.get('is_superuser', False)

        if is_superuser:
            return True

        # Менеджер ДЦ может редактировать только свою запись
        if user_profile.role_manager == 'Менеджер ДЦ':
            return user_instance == user_profile.user

        # Владелец (owner) может редактировать только пользователей из своей организации
        if user_profile.role_manager == 'owner':
            return user_instance.userprofile.organization_manager == user_profile.organization_manager

        return False
