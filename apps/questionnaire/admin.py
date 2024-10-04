from django.contrib import admin

from .models import *

# Для каждой модели добавляем поле client_id
from apps.users.models import Dealership


def get_client_id(obj):
    return obj.client.id if hasattr(obj, 'client') and obj.client else None


get_client_id.short_description = 'Client ID'


@admin.register(PhoneType)
class PhoneTypeAdmin(admin.ModelAdmin):
    list_display = ('phone_type',)
    search_fields = ('phone_type',)


@admin.register(ClientPreData)
class PreDataClientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name_to_contact_pre_client', 'type_pre_client', 'product_pre_client', 'phone_number_pre_client')
    search_fields = (
        'first_name_to_contact_pre_client', 'type_pre_client', 'product_pre_client', 'phone_number_pre_client')


@admin.register(DocumentType)
class TypeDocumentAdmin(admin.ModelAdmin):
    list_display = ('document_type',)
    search_fields = ('document_type',)


@admin.register(ClientDocument)
class ClientUploadDocumentAdmin(admin.ModelAdmin):
    list_display = ('client', 'document_type', 'uploaded_at', get_client_id)
    search_fields = ('client', 'document_type', 'uploaded_at')


@admin.register(FinancingTerm)
class FinancingTermAdmin(admin.ModelAdmin):
    list_display = ('term',)
    search_fields = ('term',)


@admin.register(ClientFinancingCondition)
class FinancingConditionsAdmin(admin.ModelAdmin):
    list_display = ('client', 'initial_payment', 'financing_term', 'monthly_payment', 'deferred_payment', get_client_id)
    search_fields = ('client', 'initial_payment', 'financing_term', 'monthly_payment', 'deferred_payment')


@admin.register(CarBrand)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(CarCondition)
class CarConditionAdmin(admin.ModelAdmin):
    list_display = ('condition',)
    search_fields = ('condition',)


@admin.register(CarConfiguration)
class CarConfigurationAdmin(admin.ModelAdmin):
    list_display = ('configuration',)
    search_fields = ('configuration',)


@admin.register(EngineType)
class EngineTypeAdmin(admin.ModelAdmin):
    list_display = ('engine_type',)
    search_fields = ('engine_type',)


@admin.register(EcoClass)
class EcoClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


@admin.register(ClientCarInfo)
class CarInfoAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'brand_car_info', 'model_car_info', 'condition_car_info',
        'configuration_car_info', 'year_car_info', 'engine_volume_car_info',
        'power_car_info', 'color_car_info', 'mileage_car_info',
        'engine_type_car_info', 'vin_car_info', 'car_price_car_info',
        'dealer_equipment_price_car_info', 'price_date_car_info',
        'body_number_car_info', 'engine_number_car_info', 'eco_class_car_info', get_client_id
    )
    search_fields = (
        'client__name', 'brand_car_info__name', 'model_car_info',
        'condition_car_info__name', 'configuration_car_info',
        'year_car_info', 'engine_volume_car_info', 'power_car_info',
        'color_car_info', 'mileage_car_info', 'engine_type_car_info__name',
        'vin_car_info', 'car_price_car_info', 'dealer_equipment_price_car_info',
        'body_number_car_info', 'engine_number_car_info', 'eco_class_car_info__name'
    )


@admin.register(TypePts)
class TypePtsAdmin(admin.ModelAdmin):
    list_display = ('pts_type',)
    search_fields = ('pts_type',)


@admin.register(AutoSaleDocument)
class DocumentSaleAutoAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'pts_type_sale_auto', 'pts_number_sale_auto', 'pts_issue_sale_auto', 'pts_issued_by_sale_auto',
        'pts_name_sale_auto', 'dcp_number_sale_auto', 'dcp_issue_date_sale_auto', get_client_id)
    search_fields = (
        'client', 'pts_type_sale_auto', 'pts_number_sale_auto', 'pts_issue_sale_auto', 'pts_issued_by_sale_auto',
        'pts_name_sale_auto', 'dcp_number_sale_auto', 'dcp_issue_date_sale_auto')


@admin.register(ClientExtraInsurance)
class ExtraInsuranceAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'kasko_amount', 'kasko_amount_include', 'gap_amount', 'gap_amount_include', 'szh_amount', 'szh_term',
        'szh_term_include', 'financial_products_amount', 'financial_products_amount_include',
        'installment_commission_include', 'sms_notification_include', get_client_id)
    search_fields = (
        'client', 'kasko_amount', 'kasko_amount_include', 'gap_amount', 'gap_amount_include', 'szh_amount', 'szh_term',
        'szh_term_include', 'financial_products_amount', 'financial_products_amount_include',
        'installment_commission_include', 'sms_notification_include')


@admin.register(AllApplications)
class AllApplicationsAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'status', 'type_all_app', 'financing', 'manager', 'dealership_all_app', 'organization',
        'date_create_all_app', 'date_changes_all_app', get_client_id)
    search_fields = (
        'client', 'financing_conditions', 'car_info', 'documents', 'extra_insurance', 'status', 'type_all_app',
        'financing', 'manager', 'dealership_all_app', 'organization', 'date_create_all_app', 'date_changes_all_app')


@admin.register(Offers)
class OffersAdmin(admin.ModelAdmin):
    list_display = ('title', 'name_bank', 'term', 'stavka', 'pay')
    search_fields = ('title', 'name_bank', 'term', 'stavka', 'pay')


@admin.register(ClientOffer)
class OffersClientAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'client', 'offer_id', 'title_offer', 'name_bank_offer', 'term_offer', 'stavka_offer', 'pay_offer',
        get_client_id)
    search_fields = ('client', 'offer_id', 'title_offer', 'name_bank_offer', 'term_offer', 'stavka_offer', 'pay_offer')


@admin.register(SelectedClientOffer)
class SelectOffersClientAdmin(admin.ModelAdmin):
    list_display = (
        'id', get_client_id, 'client', 'offer_id', 'total_loan_amount_select', 'car_price_display_select',
        'initial_payment_select',
        'term_select', 'monthly_payment_select', 'stavka_select', 'status_select_offer', 'info_from_bank',
        'id_app_bank', 'id_app_in_system', 'link_to_detail_from_bank')
    search_fields = (
        'client', 'offer_id', 'total_loan_amount_select', 'car_price_display_select', 'initial_payment_select',
        'term_select', 'monthly_payment_select', 'stavka_select', 'status_select_offer', 'info_from_bank',
        'id_app_bank', 'id_app_in_system', 'link_to_detail_from_bank')


@admin.register(HousingType)
class HousingTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('gender',)
    search_fields = ('gender',)


@admin.register(SocialStatus)
class SocialStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
    search_fields = ('status',)


@admin.register(ClientPersonalInfo)
class ClientInfoPersonalAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'first_name_to_contact_client', 'first_name_client', 'last_name_client', 'middle_name_client',
        'type_client', 'product_client', 'birth_date_client', 'registration_address_client', 'housing_type_client',
        'registration_date_client', 'gender_choice_client', 'social_status_client', get_client_id)
    search_fields = (
        'client', 'first_name_to_contact_client', 'first_name_client', 'last_name_client', 'middle_name_client',
        'type_client', 'product_client', 'birth_date_client', 'registration_address_client', 'housing_type_client',
        'registration_date_client', 'gender_choice_client', 'social_status_client')


@admin.register(ClientContact)
class ContactClientAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'living_address_contact', 'housing_type_contact', 'living_start_date_contact', 'phone_number_contact',
        'phone_type_contact', 'email_contact', 'notes_contact', get_client_id)
    search_fields = (
        'client', 'living_address_contact', 'housing_type_contact', 'living_start_date_contact', 'phone_number_contact',
        'phone_type_contact', 'email_contact', 'notes_contact')


@admin.register(ClientPassport)
class PassportClientAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'series_number_passport', 'issue_date_passport', 'division_code_passport', 'issued_by_passport',
        get_client_id)
    search_fields = (
        'client', 'series_number_passport', 'issue_date_passport', 'division_code_passport', 'issued_by_passport')


@admin.register(ClientDriverLicense)
class DriverLicenseAdmin(admin.ModelAdmin):
    list_display = ('client', 'series_number_driver_license', 'issue_date_driver_license', 'issued_by_driver_license',
                    'experience_start_date_driver_license', get_client_id)
    search_fields = ('client', 'series_number_driver_license', 'issue_date_driver_license', 'issued_by_driver_license',
                     'experience_start_date_driver_license')


@admin.register(ClientTaxDocument)
class TaxDocumentAdmin(admin.ModelAdmin):
    list_display = ('client', 'series_number_tax_document', 'number_tax_document', get_client_id)
    search_fields = ('client', 'series_number_tax_document', 'number_tax_document')


@admin.register(ClientPensionCertificate)
class PensionCertificateAdmin(admin.ModelAdmin):
    list_display = ('client', 'number_pension_sert', get_client_id)
    search_fields = ('client', 'number_pension_sert')


@admin.register(ClientInternationalPassport)
class InternationalPassportAdmin(admin.ModelAdmin):
    list_display = ('client', 'series_number_international_passport', 'issue_date_international_passport',
                    'issued_by_international_passport', get_client_id)
    search_fields = ('client', 'series_number_international_passport', 'issue_date_international_passport',
                     'issued_by_international_passport')


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ('level',)
    search_fields = ('level',)


@admin.register(ClientEducation)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('client', 'education_level_client', get_client_id)
    search_fields = ('client', 'education_level_client')


@admin.register(OrganizationType)
class OrganizationTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)


@admin.register(ActivityCode)
class ActivityCodeAdmin(admin.ModelAdmin):
    list_display = ('code',)
    search_fields = ('code',)


@admin.register(PositionType)
class PositionTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)


@admin.register(ClientEmployment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'organization_inn', 'organization_form', 'organization_name', 'organization_type', 'activity_code',
        'position', 'position_type', 'registration_address_employment', 'phone_number_organization',
        'current_experience', 'total_experience', 'shift_method', 'official_position', get_client_id)
    search_fields = (
        'client', 'organization_inn', 'organization_form', 'organization_name', 'organization_type', 'activity_code',
        'position', 'position_type', 'registration_address_employment', 'phone_number_organization',
        'current_experience', 'total_experience', 'shift_method', 'official_position')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ClientCitizenship)
class CitizenshipAdmin(admin.ModelAdmin):
    list_display = ('client', 'birth_country_client', 'russian_citizenship', 'residence_permit', 'us_citizenship',
                    'birth_place_citizenship', 'tax_resident_foreign', 'tax_residence_countries', 'foreign_inn',
                    get_client_id)
    search_fields = ('client', 'birth_country_client', 'russian_citizenship', 'residence_permit', 'us_citizenship',
                     'birth_place_citizenship', 'tax_resident_foreign', 'tax_residence_countries', 'foreign_inn')


@admin.register(MaritalStatus)
class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
    search_fields = ('status',)


@admin.register(PurchaseMethod)
class PurchaseMethodAdmin(admin.ModelAdmin):
    list_display = ('method',)
    search_fields = ('method',)


@admin.register(RealEstateType)
class RealEstateTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)
    search_fields = ('type',)


@admin.register(ClientFamilyInfo)
class FamilyInfoAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'marital_status', 'children_under_18', 'dependents', 'years_married', 'official_position_relative',
        'degree_of_kinship', 'relative_position', get_client_id)
    search_fields = (
        'client', 'marital_status', 'children_under_18', 'dependents', 'years_married', 'official_position_relative',
        'degree_of_kinship', 'relative_position')


@admin.register(ClientFinancialInfo)
class FinancialInfoAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'income_amount', 'confirmed_income_amount', 'income_proof_document', 'income_source',
        'disposable_income', 'spouse_income', get_client_id)
    search_fields = (
        'client', 'income_amount', 'confirmed_income_amount', 'income_proof_document', 'income_source',
        'disposable_income', 'spouse_income')


@admin.register(ClientExpenses)
class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('client', 'mandatory_payments', 'loan_payments', 'mortgage_payments', get_client_id)
    search_fields = ('client', 'mandatory_payments', 'loan_payments', 'mortgage_payments')


@admin.register(ClientVehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'brand_vehicle', 'year_vehicle', 'model_vehicle', 'purchase_year', 'purchase_method_vehicle',
        get_client_id)
    search_fields = (
        'client', 'brand_vehicle', 'year_vehicle', 'model_vehicle', 'purchase_year', 'purchase_method_vehicle')


@admin.register(ClientRealEstate)
class RealEstateAdmin(admin.ModelAdmin):
    list_display = ('client', 'real_estate_type', 'purchase_method_real_estate', 'address_real_estate',
                    'matches_registration_address_real_estate', get_client_id)
    search_fields = ('client', 'real_estate_type', 'purchase_method_real_estate', 'address_real_estate',
                     'matches_registration_address_real_estate')
