from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from typing import Dict, Any, Optional, Tuple
from django.shortcuts import get_object_or_404

from apps.questionnaire.forms.car_application_form import ExtraForm, DocumentAutoForm, PreDataClientForm, \
    FinancingConditionsForm, CarInfoForm
from apps.questionnaire.models import ClientPreData, AllApplications, SelectedClientOffer, ClientExtraInsurance, \
    ClientFinancingCondition, ClientCarInfo, AutoSaleDocument


class QuestionnaireGetHandler:
    """Обработчик GET-запросов для получения данных клиента и отображения их в шаблоне."""

    @staticmethod
    def handle(client_id: Optional[int], id_app_in_system: Optional[str], id_app_bank: Optional[str], user,
               dealership_name: Optional[str] = None) -> Tuple[Optional[HttpResponseRedirect], Dict[str, Any]]:
        if client_id:
            context = ClientDataService.get_client_data(client_id, id_app_in_system, id_app_bank)
            return None, context
        else:
            client, context = ClientCreationService.create_new_client(user, dealership_name)
            return HttpResponseRedirect(reverse('car_form', kwargs={'pk': client.pk})), {}


class QuestionnairePostHandler:
    """Обработчик POST-запросов для обработки данных форм клиента."""

    @staticmethod
    def handle(client_id: int, form_data: Dict[str, Any], ignore_required: bool) -> Dict[str, Any]:
        result = FormProcessingService.process_forms(client_id, form_data, ignore_required)

        if result.get('success'):
            return {'success': True}
        else:
            return result


class ClientDataService:
    """Сервис для получения и подготовки данных клиента и связанных объектов."""

    @staticmethod
    def get_client_data(client_id: int, id_app_in_system: Optional[str] = None, id_app_bank=None):
        client = get_object_or_404(ClientPreData, pk=client_id)
        application = get_object_or_404(AllApplications, client=client)

        context = {
            'client_id': client.id,
            'application': application,
            'extra': ExtraForm(instance=client.extra_insurance.first()),
            'document': DocumentAutoForm(instance=client.documents.first()),
            'pre_data_client': PreDataClientForm(instance=client),
            'fin_cond': FinancingConditionsForm(instance=client.financing_conditions.first()),
            'car_form': CarInfoForm(instance=client.car_info.first()),
            'id_app_in_system': id_app_in_system,
            'id_app_bank': id_app_bank,
            'hide_controls': True,
        }

        if id_app_in_system:
            select_offer = get_object_or_404(SelectedClientOffer, id_app_in_system=id_app_in_system)
            offer_data = {'offer': select_offer}
            context.update(offer_data)

        return context


class FormProcessingService:
    """Сервис для валидации и сохранения данных из форм клиента."""

    @staticmethod
    def process_forms(client_id: int, form_data: Dict[str, Any], ignore_required: bool) -> Dict[str, Any]:
        client = get_object_or_404(ClientPreData, id=client_id)

        extra = ExtraForm(form_data, instance=client.extra_insurance.first())
        document_form = DocumentAutoForm(form_data, instance=client.documents.first())
        pre_data_client = PreDataClientForm(form_data, instance=client)
        fin_cond = FinancingConditionsForm(form_data, instance=client.financing_conditions.first())
        car_form = CarInfoForm(form_data, instance=client.car_info.first())

        forms = [extra, document_form, pre_data_client, fin_cond, car_form]

        if ignore_required:
            for form in forms:
                for field in form.fields.values():
                    field.required = False

        if all([form.is_valid() for form in forms]):
            application = pre_data_client.save(commit=False)
            application.car_price_display = form_data.get('car_price_display')
            application.additional_equipment_price_display = form_data.get('additional_equipment_price_display')
            application.total_loan_amount = form_data.get('total_loan_amount')
            application.save()

            for form in forms:
                form.save()

            return {'success': True}

        else:
            context = {
                'client_id': client.id,
                'extra': extra,
                'document': document_form,
                'pre_data_client': pre_data_client,
                'fin_cond': fin_cond,
                'car_form': car_form
            }
            return context


class ClientCreationService:
    """Сервис для создания нового клиента и связанных объектов."""

    @staticmethod
    def create_new_client(user, dealership_name: Optional[str] = None) -> Tuple[ClientPreData, Dict[str, Any]]:
        forms = {
            'client_temp_form': PreDataClientForm(),
            'car_form': CarInfoForm(),
            'document_form': DocumentAutoForm(),
            'financing_conditions_form': FinancingConditionsForm(),
            'extra_form': ExtraForm()
        }

        client = ClientPreData.objects.create(
            **{field_name: forms['client_temp_form'].fields[field_name].initial for field_name in
               forms['client_temp_form'].fields}
        )

        extra_insurance = ClientExtraInsurance.objects.create(
            client=client,
            **{field_name: forms['extra_form'].fields[field_name].initial for field_name in forms['extra_form'].fields}
        )

        financing_conditions = ClientFinancingCondition.objects.create(
            client=client,
            **{field_name: forms['financing_conditions_form'].fields[field_name].initial for field_name in
               forms['financing_conditions_form'].fields}
        )
        car_info = ClientCarInfo.objects.create(
            client=client,
            **{field_name: forms['car_form'].fields[field_name].initial for field_name in forms['car_form'].fields}
        )

        document = AutoSaleDocument.objects.create(
            client=client,
            **{field_name: forms['document_form'].fields[field_name].initial for field_name in
               forms['document_form'].fields}
        )

        AllApplications.objects.create(
            client=client,
            financing_conditions=financing_conditions,
            car_info=car_info,
            documents=document,
            extra_insurance=extra_insurance,
            status=' ',
            type_all_app=client.type_pre_client,
            financing=client.product_pre_client,
            manager=user.email,
            dealership_all_app=dealership_name,
            organization=user.userprofile.organization_manager,
        )

        context = {
            'extra': forms['extra_form'],
            'document': forms['document_form'],
            'client_temp': forms['client_temp_form'],
            'fin_cond': forms['financing_conditions_form'],
            'car_form': forms['car_form'],
            'client_id': client.id,
        }

        return client, context
