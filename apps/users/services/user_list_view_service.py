from django.contrib.auth.models import User

from credit_v0.models import UserProfile


class UserViewListService:
    """Сервис для работы с пользователями"""

    @staticmethod
    def get_filtered_users(user, ordering='username'):
        """Получение пользователей с фильтрацией"""
        user_profile = UserProfile.objects.get(user=user)
        user_organization = user_profile.organization_manager

        if user.is_superuser:
            object_list = User.objects.all().select_related('userprofile').order_by(ordering)
        else:
            object_list = User.objects.filter(userprofile__organization_manager=user_organization).select_related(
                'userprofile').order_by(ordering)

        return object_list
