from django.contrib import admin

# Register your models here.
from apps.users.models import UserDocumentType, UserProfile, Dealership


@admin.register(UserDocumentType)
class UserTypeDocumentAdmin(admin.ModelAdmin):
    list_display = ('document_type',)
    search_fields = ('document_type',)


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'first_name_manager', 'last_name_manager', 'middle_name_manager', 'organization_manager',
        'role_manager', 'date_of_birth_manager', 'phone_number_manager', 'status_manager', 'passport_series_manager',
        'passport_number_manager', 'division_code_manager', 'issued_by_manager', 'issue_date_manager')
    search_fields = (
        'user', 'first_name_manager', 'last_name_manager', 'middle_name_manager', 'organization_manager',
        'role_manager', 'date_of_birth_manager', 'phone_number_manager', 'status_manager', 'passport_series_manager',
        'passport_number_manager', 'division_code_manager', 'issued_by_manager', 'issue_date_manager')


@admin.register(Dealership)
class DealershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'organisation_name')
    search_fields = ('name', 'organisation_name')