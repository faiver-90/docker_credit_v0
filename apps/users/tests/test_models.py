import pytest
from django.contrib.auth.models import User

from apps.users.models import UserProfile


class TestUsers:
    @pytest.fixture
    def create_user(self):
        return User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    @pytest.mark.django_db
    def test_user_create(self, create_user):
        assert User.objects.count() == 1
        assert User.objects.filter(username='john').exists()

    @pytest.mark.django_db
    def test_create_profile(self, create_user):
        user = create_user
        profile = UserProfile.objects.create(
            user=user,
            first_name_manager='Иван',
            last_name_manager='Иванов',
            middle_name_manager='Иванович',
            organization_manager='ООО Компания',
            role_manager='Менеджер',
            date_of_birth_manager='1980-01-01',
            phone_number_manager='+71234567890',
            status_manager=True,
            passport_series_manager='1234',
            passport_number_manager='567890',
            division_code_manager='123-456',
            issued_by_manager='ОВД г. Москва',
            issue_date_manager='2000-01-01'
        )

        assert profile.user == user
        assert profile.first_name_manager == 'Иван'
        assert profile.last_name_manager == 'Иванов'
        assert profile.phone_number_manager == '+71234567890'

    @pytest.mark.django_db
    def test_delete_user(self, create_user):
        User.objects.filter(username='john').delete()
        assert User.objects.count() == 0
