from credit_v0.forms.car_application_form import ClientInfoPersonalForm, FinancingConditionsForm, CarInfoForm, \
    DocumentAutoForm, PassportClientForm, ExtraForm, ContactClientForm, DriverLicenseForm, TaxDocumentForm, \
    PensionCertificateForm, EducationForm, EmploymentForm, CitizenshipForm, FamilyInfoForm, FinancialInfoForm, \
    ExpensesForm, VehicleForm, RealEstateForm, InternationalPassportForm
from credit_v0.forms.upload_file_form import ClientUploadDocumentForm
from credit_v0.models import ClientDocument, SelectedClientOffer


class ClientExtraDataService:
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

    def __init__(self, client, data=None):
        self.client = client
        self.data = data

    def get_client_context(self):
        context = {}
        for attr, form_class in self.forms_map.items():
            instance = getattr(self.client, attr).first()
            context[f'{attr}_form'] = form_class(instance=instance)
        context['document_form'] = ClientUploadDocumentForm()
        context['client_documents'] = ClientDocument.objects.filter(client=self.client)
        return context

    def prepare_forms(self):
        forms = {}
        for attr, form_class in self.forms_map.items():
            instance = getattr(self.client, attr).first()
            forms[attr] = form_class(self.data, instance=instance)
        return forms

    @staticmethod
    def set_fields_not_required(forms):
        for form in forms.values():
            for field in form.fields.values():
                field.required = False

    def save_forms(self, forms):
        for form in forms.values():
            form.save_or_update(client_id=self.client.id)


class BankOfferService:
    @staticmethod
    def prepare_offer_data(client_id, offer_ids):
        """Готовит данные для отправки в Kafka"""

        return {
            'client_id': client_id,
            'selected_offers': offer_ids
        }

    @staticmethod
    def process_offers(client_id, offer_ids):
        """Обновляет статус предложений клиента на 'Одобрение'."""

        for offer_id in offer_ids:
            offers = SelectedClientOffer.objects.filter(offer_id=offer_id, client_id=client_id)
            if offers.exists():
                for offer in offers:
                    offer.status_select_offer = 'Одобрение'
                    offer.save()
            else:
                print(f'Offer with id {offer_id} does not exist for client {client_id}')

    @staticmethod
    def check_if_saved(client_id, selected_offers):
        for offer_id in selected_offers:
            if not SelectedClientOffer.objects.filter(client_id=client_id,
                                                      offer_id=offer_id,
                                                      status_select_offer='Одобрение').exists():
                return False
        return True