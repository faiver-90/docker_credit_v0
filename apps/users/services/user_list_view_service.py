from django.contrib.auth.models import User

from apps.users.models import UserProfile


class UserViewListService:
    """Сервис для работы с пользователями"""

    @staticmethod
    def get_filtered_users(user, ordering='username'):
        """Получение пользователей с фильтрацией"""
        if user.is_superuser:
            return User.objects.all().select_related('userprofile').order_by(ordering)

        user_profile = UserProfile.objects.get(user=user)
        user_organization = user_profile.organization_manager

        if user_organization:
            return User.objects.filter(
                userprofile__organization_manager=user_organization
            ).select_related('userprofile').order_by(ordering)

        return User.objects.none()
