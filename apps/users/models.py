import os

from django.contrib.auth.models import User
from django.db import models
from text_unidecode import unidecode


def user_upload_to(instance, filename):
    filename = unidecode(filename)
    return os.path.join(f'user_documents/user_{instance.user.id}', filename)


class UserDocumentType(models.Model):
    document_type = models.CharField(max_length=50, unique=True, verbose_name="Тип документа")

    class Meta:
        verbose_name = "Тип документа пользователя"
        verbose_name_plural = "Типы документов пользователей"

    def __str__(self):
        return self.document_type


class UserDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document_type = models.ForeignKey(UserDocumentType, on_delete=models.CASCADE, null=True, blank=True,
                                      verbose_name="Тип документа")
    document_file = models.FileField(upload_to=user_upload_to, verbose_name="Выбрать файл")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # def delete(self, *args, **kwargs):
    #     file_path = self.document_file.path
    #     super().delete(*args, **kwargs)
    #     if os.path.exists(file_path):
    #         os.remove(file_path)
    #
    #     folder_path = os.path.dirname(file_path)
    #     if not os.listdir(folder_path):
    #         os.rmdir(folder_path)

    class Meta:
        verbose_name = "Загруженный документ пользователя"
        verbose_name_plural = "Загруженные документы пользователей"

    def __str__(self):
        if self.document_type:
            return f"{self.document_type}"
        else:
            return f"Документ без типа ({self.user})"


class Dealership(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название дилерского центра")
    organisation_name = models.CharField(max_length=255, verbose_name="Название организации")

    # is_active = models.BooleanField(default=False, verbose_name="Активный")

    class Meta:
        verbose_name = "Дилерский центр"
        verbose_name_plural = "Дилерские центры"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name_manager = models.CharField(max_length=30, verbose_name="Имя", null=True)
    last_name_manager = models.CharField(max_length=30, verbose_name="Фамилия", null=True)
    middle_name_manager = models.CharField(max_length=30, verbose_name="Отчество", null=True)
    dealership_manager = models.ManyToManyField(Dealership, blank=True, related_name='managed_profiles',
                                                verbose_name="Дилерский центр")
    active_dealership = models.ForeignKey(Dealership, null=True, blank=True, on_delete=models.SET_NULL,
                                          related_name='active_profiles')

    organization_manager = models.CharField(max_length=255, blank=True, null=True, verbose_name="Организация")
    role_manager = models.CharField(max_length=50, verbose_name="Роль")
    date_of_birth_manager = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    phone_number_manager = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефонный номер")
    status_manager = models.BooleanField(default=True, verbose_name="Статус")

    passport_series_manager = models.CharField(max_length=10, null=True, blank=True, verbose_name="Серия паспорта")
    passport_number_manager = models.CharField(max_length=10, null=True, blank=True, verbose_name="Номер паспорта")
    division_code_manager = models.CharField(max_length=7, null=True, blank=True, verbose_name="Код подразделения")
    issued_by_manager = models.CharField(max_length=255, null=True, blank=True, verbose_name="Кем выдан")
    issue_date_manager = models.DateField(null=True, blank=True, verbose_name="Дата выдачи")

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def get_active_dealership(self):
        return self.active_dealership

    def set_active_dealership(self, dealership):
        if dealership in self.dealership_manager.all():
            self.active_dealership = dealership
            self.save()
        else:
            raise ValueError("Dealership not associated with this profile")

    def __str__(self):
        return self.user.username
