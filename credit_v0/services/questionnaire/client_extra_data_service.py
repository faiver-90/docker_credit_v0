from credit_v0.forms.car_application_form import ClientInfoPersonalForm, FinancingConditionsForm, CarInfoForm, \
    DocumentAutoForm, PassportClientForm, ExtraForm, ContactClientForm, DriverLicenseForm, TaxDocumentForm, \
    PensionCertificateForm, EducationForm, EmploymentForm, CitizenshipForm, FamilyInfoForm, FinancialInfoForm, \
    ExpensesForm, VehicleForm, RealEstateForm, InternationalPassportForm
from credit_v0.forms.upload_file_form import ClientUploadDocumentForm
from credit_v0.models import ClientDocument
from typing import Dict
from django.http import QueryDict
from django.forms import BaseForm
from django.db.models import Model


class ClientExtraDataService:
    """
        Сервис для работы с дополнительной информацией о клиенте.
    """

    forms_map = {
        'client_person_data': ClientInfoPersonalForm,
        'financing_conditions': FinancingConditionsForm,
        'car_info': CarInfoForm,
        'documents': DocumentAutoForm,
        'extra_insurance': ExtraForm,
        'passport_data': PassportClientForm,
        'contact_data': ContactClientForm,
        'driver_license_data': DriverLicenseForm,
        'tax_document': TaxDocumentForm,
        'pension_certificate': PensionCertificateForm,
        'education': EducationForm,
        'employment': EmploymentForm,
        'citizenship': CitizenshipForm,
        'family_info': FamilyInfoForm,
        'financial_info': FinancialInfoForm,
        'expenses': ExpensesForm,
        'vehicle': VehicleForm,
        'real_estate': RealEstateForm,
        'international_passport': InternationalPassportForm,
    }

    def __init__(self, client: Model):
        self.client = client

    def get_client_context(self) -> Dict[str, BaseForm]:
        context = {}
        for attr, form_class in self.forms_map.items():
            instance = getattr(self.client, attr).first()
            context[f'{attr}_form'] = form_class(instance=instance)
        context['document_form'] = ClientUploadDocumentForm()
        context['client_documents'] = ClientDocument.objects.filter(client=self.client)
        return context

    def prepare_forms(self, data: QueryDict) -> Dict[str, BaseForm]:
        forms = {}
        for attr, form_class in self.forms_map.items():
            instance = getattr(self.client, attr).first()
            forms[attr] = form_class(data, instance=instance)
        return forms

    @staticmethod
    def set_fields_not_required(forms: Dict[str, BaseForm]) -> None:
        for form in forms.values():
            for field in form.fields.values():
                field.required = False

    def save_forms(self, forms):
        for form in forms.values():
            # Предположим, что идентификатор клиента используется для поиска и обновления
            form.save_or_update(client_id=self.client.id)