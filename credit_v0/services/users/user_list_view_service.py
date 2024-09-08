from django.contrib.auth.models import User
from django.core.paginator import Paginator

from credit_v0.models import UserProfile


class UserViewListService:
    """Сервис для работы с пользователями"""

    @staticmethod
    def get_users(user, ordering='username', page_number=1, per_page=5):
        """Получение пользователей с фильтрацией и пагинацией"""
        user_profile = UserProfile.objects.get(user=user)
        user_organization = user_profile.organization_manager

        if user.is_superuser:
            object_list = User.objects.all().select_related('userprofile').order_by(ordering)
        else:
            object_list = User.objects.filter(userprofile__organization_manager=user_organization).select_related(
                'userprofile').order_by(ordering)

        paginator = Paginator(object_list, per_page)
        page_obj = paginator.get_page(page_number)

        return page_obj
