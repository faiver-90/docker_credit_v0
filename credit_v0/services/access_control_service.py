class AccessControlService:
    """Сервис для проверки доступа на основе роли пользователя."""

    @staticmethod
    def has_access(user_profile, user_instance):
        """Проверка доступа на редактирование профиля пользователя."""
        # Администратор имеет полный доступ
        if user_profile.role_manager == 'superuser':
            return True

        # Менеджер ДЦ может редактировать только свою запись
        if user_profile.role_manager == 'Менеджер ДЦ':
            return user_instance == user_profile.user

        # Владелец (owner) может редактировать только пользователей из своей организации
        if user_profile.role_manager == 'owner':
            return user_instance.userprofile.organization_manager == user_profile.organization_manager

        return False
