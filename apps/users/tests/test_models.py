import pytest
from django.contrib.auth.models import User

from django.core.files.uploadedfile import SimpleUploadedFile
from apps.users.models import UserDocumentType, UserDocument, Dealership, UserProfile
from django.db import IntegrityError


@pytest.mark.django_db
class TestUserModels:
    USERNAME = 'john'

    @classmethod
    @pytest.fixture(autouse=True)
    def setup_class(cls, db):
        cls.user = User.objects.create_user(username=cls.USERNAME, email='john@doe.com', password='password')
        cls.document_type = UserDocumentType.objects.create(document_type="Паспорт")
        cls.dealership = Dealership.objects.create(name="Автоцентр", organisation_name="ООО Авто")
        cls.dealership2 = Dealership.objects.create(name="Автоцентр2", organisation_name="ООО Авто2")
        cls.user_profile = UserProfile.objects.create(
            user=cls.user,
            first_name_manager='Иван',
            last_name_manager='Иванов',
            middle_name_manager='Иванович',
            organization_manager="ООО Компания",
            role_manager="Менеджер",
            date_of_birth_manager='1980-01-01',
            phone_number_manager='+71234567890',
            status_manager=True,
            passport_series_manager='1234',
            passport_number_manager='567890',
            division_code_manager='123-456',
            issued_by_manager='ОВД г. Москва',
            issue_date_manager='2000-01-01',
        )
        cls.user_profile.dealership_manager.set([cls.dealership, cls.dealership2])
        cls.user_profile.active_dealership = cls.dealership2
        cls.user_profile.save()

    @pytest.mark.positive
    def test_remove_dealership_from_profile(self):
        self.user_profile.dealership_manager.remove(self.dealership)
        assert self.user_profile.dealership_manager.count() == 1

    @pytest.mark.positive
    def test_delete_dealership(self):
        dealership_id = self.dealership.id
        self.dealership.delete()
        assert not Dealership.objects.filter(id=dealership_id).exists()

    @pytest.mark.positive
    def test_create_user_document_type(self):
        assert UserDocumentType.objects.count() == 1
        assert self.document_type.document_type == "Паспорт"

    @pytest.mark.positive
    def test_unique_document_type(self):
        with pytest.raises(IntegrityError):
            UserDocumentType.objects.create(document_type="Паспорт")

    @pytest.mark.positive
    def test_create_user_document(self):
        document_file = SimpleUploadedFile("file.pdf", b"file_content")
        user_document = UserDocument.objects.create(
            user=self.user,
            document_type=self.document_type,
            document_file=document_file
        )
        assert UserDocument.objects.count() == 1
        assert user_document.document_file.name.startswith('user_documents/user_')
        assert user_document.user == self.user
        assert user_document.document_type == self.document_type

    @pytest.mark.positive
    def test_create_user(self):
        assert User.objects.get(username=self.USERNAME)

    @pytest.mark.positive
    def test_create_dealership(self):
        assert Dealership.objects.count() == 2
        assert self.dealership.name == "Автоцентр"
        assert self.dealership.organisation_name == "ООО Авто"

    @pytest.mark.positive
    def test_dealership_str_method(self):
        assert str(self.dealership) == "Автоцентр"

    @pytest.mark.positive
    def test_create_user_profile(self):
        assert UserProfile.objects.count() == 1
        assert self.user_profile.user == self.user
        assert self.user_profile.first_name_manager == 'Иван'
        assert self.user_profile.dealership_manager.filter(id=self.dealership.id).exists()

    @pytest.mark.positive
    def test_set_active_dealership(self):
        self.user_profile.set_active_dealership(self.dealership)
        assert self.user_profile.get_active_dealership() == self.dealership

    @pytest.mark.positive
    def test_set_active_dealership_not_associated(self):
        other_dealership = Dealership.objects.create(name="Другой Автоцентр", organisation_name="ООО Другой Авто")
        with pytest.raises(ValueError, match="Dealership not associated with this profile"):
            self.user_profile.set_active_dealership(other_dealership)

    @pytest.mark.positive
    def test_user_profile_str_method(self):
        assert str(self.user_profile) == self.user.username

    @pytest.mark.positive
    def test_delete_user(self):
        self.user.delete()
        assert User.objects.count() == 0
        assert UserProfile.objects.count() == 0
        assert UserDocument.objects.count() == 0

    @pytest.mark.negative
    @pytest.mark.xfail
    @pytest.mark.boundary
    def test_creat_user_long_name(self):
        User.objects.create(username=151 * 'a', password='1234', email='er@er.com')

    @pytest.mark.negative
    @pytest.mark.xfail
    def test_create_user_document_without_user(self):
        document_file = SimpleUploadedFile("file.pdf", b"file_content")
        UserDocument.objects.create(
            user=None,
            document_type=self.document_type,
            document_file=document_file
        )

    @pytest.mark.negative
    @pytest.mark.xfail
    def test_create_user_document_without_file(self):
        user_document = UserDocument(
            user=self.user,
            document_type=self.document_type,
            document_file=None
        )
        user_document.full_clean()
        user_document.save()

    @pytest.mark.negative
    @pytest.mark.xfail
    def test_create_user_document_without_document_type(self):
        document_file = SimpleUploadedFile("file.pdf", b"file_content")
        user_document = UserDocument.objects.create(
            user=self.user,
            document_type=None,
            document_file=document_file
        )
        assert user_document.document_type is None

    @pytest.mark.boundary
    def test_create_user_document_with_long_filename(self):
        long_filename = "a" * 255 + ".pdf"
        document_file = SimpleUploadedFile(long_filename, b"file_content")
        user_document = UserDocument.objects.create(
            user=self.user,
            document_type=self.document_type,
            document_file=document_file
        )
        assert len(user_document.document_file.name) <= 255

    @pytest.mark.boundary
    def test_create_user_document_with_long_document_type(self):
        long_document_type = "a" * 50
        document_type = UserDocumentType.objects.create(document_type=long_document_type)
        assert len(document_type.document_type) == 50

    @pytest.mark.boundary
    def test_create_user_profile_with_max_length_first_name(self):
        user_profile = UserProfile.objects.create(
            user=self.user,
            first_name_manager='a' * 30,  # Maximum length
            last_name_manager='Иванов'
        )
        assert len(user_profile.first_name_manager) == 30