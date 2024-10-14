from django import forms
from django.db.models import IntegerField
from django.db.models.functions import Cast

from apps.questionnaire.models import (
    ClientCarInfo, ClientExtraInsurance, AutoSaleDocument, ClientPreData,
    ClientFinancingCondition, ClientPersonalInfo, ClientContact, FinancingTerm,
    ClientPassport, ClientDriverLicense, ClientTaxDocument, ClientPensionCertificate,
    ClientInternationalPassport, ClientEducation, ClientEmployment, EducationLevel,
    OrganizationType, ActivityCode, PositionType, ClientCitizenship, Country,
    ClientFamilyInfo, MaritalStatus, ClientFinancialInfo, ClientExpenses,
    ClientVehicle, PurchaseMethod, ClientRealEstate, RealEstateType, IncomeType
)


class BaseForm(forms.ModelForm):
    def save_or_update(self, **lookup):
        try:
            instance = self.Meta.model.objects.get(**lookup)
            for attr, value in self.cleaned_data.items():
                setattr(instance, attr, value)
            instance.save()
        except self.Meta.model.DoesNotExist:
            instance = self.Meta.model.objects.create(**self.cleaned_data, **lookup)

        return instance


class CarInfoForm(BaseForm):
    class Meta:
        model = ClientCarInfo
        fields = ['brand_car_info', 'model_car_info', 'condition_car_info', 'configuration_car_info', 'year_car_info',
                  'engine_volume_car_info', 'power_car_info', 'color_car_info', 'mileage_car_info',
                  'engine_type_car_info', 'vin_car_info', 'car_price_car_info', 'dealer_equipment_price_car_info',
                  'body_number_car_info', 'engine_number_car_info', 'eco_class_car_info']
        widgets = {
            'brand_car_info': forms.Select(attrs={'class': 'form-select'}),
            'model_car_info': forms.TextInput(attrs={'class': 'form-control'}),
            'engine_number_car_info': forms.TextInput(attrs={'class': 'form-control'}),
            'body_number_car_info': forms.TextInput(attrs={'class': 'form-control'}),
            'condition_car_info': forms.Select(attrs={'class': 'form-select'}),
            'configuration_car_info': forms.TextInput(attrs={'class': 'form-control'}),
            'eco_class_car_info': forms.Select(attrs={'class': 'form-select'}),
            'year_car_info': forms.TextInput(attrs={'class': 'form-control'}),
            'engine_volume_car_info': forms.TextInput(attrs={'class': 'form-control'}),
            'power_car_info': forms.TextInput(attrs={'class': 'form-control'}),
            'color_car_info': forms.TextInput(attrs={'class': 'form-control'}),
            'mileage_car_info': forms.NumberInput(attrs={'class': 'form-control'}),
            'engine_type_car_info': forms.Select(attrs={'class': 'form-select'}),
            'vin_car_info': forms.TextInput(attrs={'class': 'form-control'}),
            'car_price_car_info': forms.NumberInput(attrs={'class': 'form-control'}),
            'dealer_equipment_price_car_info': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CarInfoForm, self).__init__(*args, **kwargs)
        self.fields['model_car_info'].required = False
        self.fields['price_date_car_info'] = forms.DateTimeField(
            required=False,
            widget=forms.DateTimeInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            label='Дата формирования цены'
        )

        if self.instance and self.instance.price_date_car_info:
            self.fields['price_date_car_info'].initial = self.instance.price_date_car_info

        if self.request and self.request.path == '/credit/continue_docs/':
            for field in self.fields:
                self.fields[f'{field}'].required = True


class ExtraForm(BaseForm):
    class Meta:
        model = ClientExtraInsurance
        fields = ['kasko_amount', 'kasko_amount_include', 'gap_amount', 'gap_amount_include', 'szh_amount', 'szh_term',
                  'szh_term_include', 'financial_products_amount', 'financial_products_amount_include',
                  'installment_commission_include', 'sms_notification_include']
        widgets = {
            'kasko_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'kasko_amount_include': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'gap_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'gap_amount_include': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'szh_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'szh_term': forms.NumberInput(attrs={'class': 'form-control'}),
            'szh_term_include': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'financial_products_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'financial_products_amount_include': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'installment_commission_include': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sms_notification_include': forms.CheckboxInput(
                attrs={'class': 'form-check-input', 'id': 'sms_notification_include_checkbox'}),
        }


class DocumentAutoForm(BaseForm):
    class Meta:
        model = AutoSaleDocument
        fields = [
            'pts_type_sale_auto', 'pts_number_sale_auto', 'pts_issue_sale_auto', 'pts_issued_by_sale_auto',
            'pts_name_sale_auto', 'dcp_number_sale_auto', 'dcp_issue_date_sale_auto'
        ]
        widgets = {
            'pts_type_sale_auto': forms.Select(attrs={'class': 'form-select'}),
            'pts_number_sale_auto': forms.NumberInput(attrs={'class': 'form-control'}),
            'pts_issue_sale_auto': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'pts_issued_by_sale_auto': forms.TextInput(attrs={'class': 'form-control'}),
            'pts_name_sale_auto': forms.TextInput(attrs={'class': 'form-control'}),
            'dcp_number_sale_auto': forms.NumberInput(attrs={'class': 'form-control'}),
            'dcp_issue_date_sale_auto': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(DocumentAutoForm, self).__init__(*args, **kwargs)

        if self.request and self.request.path == '/credit/continue_docs/':
            for field in self.fields:
                self.fields[f'{field}'].required = True

    @property
    def pts_fields(self):
        return [self[field] for field in self.fields if field.startswith('pts')]

    @property
    def dcp_fields(self):
        return [self[field] for field in self.fields if field.startswith('dcp')]


class PreDataClientForm(BaseForm):
    class Meta:
        model = ClientPreData
        fields = ['first_name_to_contact_pre_client', 'type_pre_client', 'product_pre_client',
                  'phone_number_pre_client', 'type_phone_pre_client']
        widgets = {
            'first_name_to_contact_pre_client': forms.TextInput(attrs={'class': 'form-control'}),
            'type_pre_client': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'product_pre_client': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'phone_number_pre_client': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '+7 (123) 456-78-90'}),
            'type_phone_pre_client': forms.Select(attrs={'class': 'form-select'}),
        }


class FinancingConditionsForm(BaseForm):
    class Meta:
        model = ClientFinancingCondition
        fields = ['initial_payment', 'financing_term', 'monthly_payment', 'deferred_payment']
        widgets = {
            'initial_payment': forms.NumberInput(attrs={'class': 'form-control'}),
            'financing_term': forms.Select(attrs={'class': 'form-select'}),
            'monthly_payment': forms.NumberInput(attrs={'class': 'form-control'}),
            'deferred_payment': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(FinancingConditionsForm, self).__init__(*args, **kwargs)
        self.fields['financing_term'].queryset = FinancingTerm.objects.annotate(
            numeric_value=Cast('term', IntegerField())).order_by('numeric_value')
        self.fields['financing_term'].required = False


# Start additional form
class ClientInfoPersonalForm(BaseForm):
    class Meta:
        model = ClientPersonalInfo

        fields = [
            'first_name_to_contact_client', 'first_name_client', 'last_name_client', 'middle_name_client',
            'type_client', 'product_client', 'birth_date_client', 'registration_address_client', 'housing_type_client',
            'registration_date_client', 'gender_choice_client',
            'social_status_client', 'country_name_pre_client', 'post_code'
        ]
        widgets = {
            'first_name_to_contact_client': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name_client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'last_name_client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
            'middle_name_client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отчество'}),
            'type_client': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'product_client': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'birth_date_client': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'registration_address_client': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите адрес'}),
            'housing_type_client': forms.Select(attrs={'class': 'form-select'}),
            'registration_date_client': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender_choice_client': forms.Select(attrs={'class': 'form-select'}),
            'social_status_client': forms.Select(attrs={'class': 'form-select'}),
            'country_name_pre_client': forms.TextInput(attrs={'class': 'form-control'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(ClientInfoPersonalForm, self).__init__(*args, **kwargs)
        self.fields['first_name_client'].required = True
        self.fields['last_name_client'].required = True
        # self.fields['type_client'].initial = 'Физическое лицо'
        # self.fields['product_client'].initial = 'Кредит'


class ContactClientForm(BaseForm):
    class Meta:
        model = ClientContact
        fields = ['living_address_contact', 'housing_type_contact', 'living_start_date_contact', 'phone_number_contact',
                  'phone_type_contact',
                  'email_contact', 'notes_contact']
        widgets = {
            'living_address_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите адрес'}),
            'housing_type_contact': forms.Select(attrs={'class': 'form-select'}),
            'living_start_date_contact': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'phone_number_contact': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '+7 (123) 456-78-90'}),
            'phone_type_contact': forms.Select(attrs={'class': 'form-select'}),
            'email_contact': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@domain.com'}),
            'notes_contact': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PassportClientForm(BaseForm):
    class Meta:
        model = ClientPassport
        fields = ['series_number_passport', 'issue_date_passport', 'division_code_passport', 'issued_by_passport']
        widgets = {
            'series_number_passport': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '____ ______'}),
            'issue_date_passport': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'division_code_passport': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '___-___'}),
            'issued_by_passport': forms.TextInput(attrs={'class': 'form-control'}),
        }


class DriverLicenseForm(BaseForm):
    class Meta:
        model = ClientDriverLicense
        fields = ['series_number_driver_license', 'issue_date_driver_license', 'issued_by_driver_license',
                  'experience_start_date_driver_license']
        widgets = {
            'series_number_driver_license': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "__ __ ______"}),
            'issue_date_driver_license': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'issued_by_driver_license': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_start_date_driver_license': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class TaxDocumentForm(BaseForm):
    class Meta:
        model = ClientTaxDocument
        fields = ['series_number_tax_document', 'number_tax_document']
        widgets = {
            'series_number_tax_document': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "____ ______"}),
            'number_tax_document': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "____________"}),
        }


class PensionCertificateForm(BaseForm):
    class Meta:
        model = ClientPensionCertificate
        fields = ['number_pension_sert']
        widgets = {
            'number_pension_sert': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "___-___-___ __", }),
        }


class InternationalPassportForm(BaseForm):
    class Meta:
        model = ClientInternationalPassport
        fields = ['series_number_international_passport', 'issue_date_international_passport',
                  'issued_by_international_passport']
        widgets = {
            'series_number_international_passport': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': "__ _______", }),
            'issue_date_international_passport': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'issued_by_international_passport': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EducationForm(BaseForm):
    class Meta:
        model = ClientEducation
        fields = ['education_level_client']
        widgets = {
            'education_level_client': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        # Сортировка по строковому значению уровня образования
        self.fields['education_level_client'].queryset = EducationLevel.objects.order_by('level')


class EmploymentForm(BaseForm):
    class Meta:
        model = ClientEmployment
        fields = ['organization_inn', 'organization_form', 'organization_name', 'organization_type', 'activity_code',
                  'position', 'position_type', 'registration_address_employment', 'phone_number_organization',
                  'current_experience',
                  'total_experience', 'shift_method', 'official_position']
        widgets = {
            'organization_inn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "__________", }),
            'organization_form': forms.TextInput(attrs={'class': 'form-control'}),
            'organization_name': forms.TextInput(attrs={'class': 'form-control'}),
            'organization_type': forms.Select(attrs={'class': 'form-select'}),
            'activity_code': forms.Select(attrs={'class': 'form-select'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'position_type': forms.Select(attrs={'class': 'form-select'}),
            'registration_address_employment': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number_organization': forms.TextInput(attrs={'class': 'form-control'}),
            'current_experience': forms.TextInput(attrs={'class': 'form-control'}),
            'total_experience': forms.TextInput(attrs={'class': 'form-control'}),
            'shift_method': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'official_position': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmploymentForm, self).__init__(*args, **kwargs)
        self.fields['organization_type'].queryset = OrganizationType.objects.order_by('type')
        self.fields['activity_code'].queryset = ActivityCode.objects.order_by('code')
        self.fields['position_type'].queryset = PositionType.objects.order_by('type')


class CitizenshipForm(BaseForm):
    class Meta:
        model = ClientCitizenship
        fields = ['birth_country_client', 'russian_citizenship', 'residence_permit', 'us_citizenship',
                  'birth_place_citizenship',
                  'tax_resident_foreign', 'tax_residence_countries', 'foreign_inn']
        widgets = {
            'birth_country_client': forms.Select(attrs={'class': 'form-select'}),
            'russian_citizenship': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'residence_permit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'us_citizenship': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'birth_place_citizenship': forms.TextInput(attrs={'class': 'form-control'}),
            'tax_resident_foreign': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'tax_residence_countries': forms.TextInput(attrs={'class': 'form-control'}),
            'foreign_inn': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CitizenshipForm, self).__init__(*args, **kwargs)
        self.fields['birth_country_client'].queryset = Country.objects.order_by('name')


class FamilyInfoForm(BaseForm):
    class Meta:
        model = ClientFamilyInfo
        fields = ['marital_status', 'children_under_18', 'dependents', 'years_married', 'official_position_relative',
                  'degree_of_kinship', 'relative_position']
        widgets = {
            'marital_status': forms.Select(attrs={'class': 'form-select'}),
            'children_under_18': forms.NumberInput(attrs={'class': 'form-control'}),
            'dependents': forms.NumberInput(attrs={'class': 'form-control'}),
            'years_married': forms.NumberInput(attrs={'class': 'form-control'}),
            'official_position_relative': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'degree_of_kinship': forms.TextInput(attrs={'class': 'form-control'}),
            'relative_position': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(FamilyInfoForm, self).__init__(*args, **kwargs)
        self.fields['marital_status'].queryset = MaritalStatus.objects.order_by('status')


class FinancialInfoForm(BaseForm):
    class Meta:
        model = ClientFinancialInfo
        fields = ['income_type', 'income_amount', 'confirmed_income_amount', 'income_proof_document', 'income_source',
                  'disposable_income', 'spouse_income']
        widgets = {
            'income_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'confirmed_income_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'income_proof_document': forms.TextInput(attrs={'class': 'form-control'}),
            'income_source': forms.TextInput(attrs={'class': 'form-control'}),
            'disposable_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'spouse_income': forms.NumberInput(attrs={'class': 'form-control'}),
            'income_type': forms.Select(attrs={'class': 'form-select'})
        }

    def __init__(self, *args, **kwargs):
        super(FinancialInfoForm, self).__init__(*args, **kwargs)
        self.fields['income_type'].queryset = IncomeType.objects.order_by('type')


class ExpensesForm(BaseForm):
    class Meta:
        model = ClientExpenses
        fields = ['mandatory_payments', 'loan_payments', 'mortgage_payments']
        widgets = {
            'mandatory_payments': forms.NumberInput(attrs={'class': 'form-control'}),
            'loan_payments': forms.NumberInput(attrs={'class': 'form-control'}),
            'mortgage_payments': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class VehicleForm(BaseForm):
    class Meta:
        model = ClientVehicle
        fields = ['brand_vehicle', 'year_vehicle', 'model_vehicle', 'purchase_year', 'purchase_method_vehicle']
        widgets = {
            'brand_vehicle': forms.TextInput(attrs={'class': 'form-control'}),
            'year_vehicle': forms.TextInput(attrs={'class': 'form-control'}),
            'model_vehicle': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_year': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_method_vehicle': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(VehicleForm, self).__init__(*args, **kwargs)
        self.fields['purchase_method_vehicle'].queryset = PurchaseMethod.objects.order_by('method')


class RealEstateForm(BaseForm):
    class Meta:
        model = ClientRealEstate
        fields = ['real_estate_type', 'purchase_method_real_estate', 'address_real_estate',
                  'matches_registration_address_real_estate']
        widgets = {
            'real_estate_type': forms.Select(attrs={'class': 'form-select'}),
            'purchase_method_real_estate': forms.Select(attrs={'class': 'form-select'}),
            'address_real_estate': forms.TextInput(attrs={'class': 'form-control'}),
            'matches_registration_address_real_estate': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super(RealEstateForm, self).__init__(*args, **kwargs)
        self.fields['real_estate_type'].queryset = RealEstateType.objects.order_by('type')
        self.fields['purchase_method_real_estate'].queryset = PurchaseMethod.objects.order_by('method')
