from django.shortcuts import get_object_or_404

from app_v0.settings import BASE_DIR
from apps.core.banking_services.building_bank_requests_service import (
    CommonBankBuildingRequestsService,
    CommonValidateFieldService)
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_connect_api_service import \
    SovcombankRequestService
from apps.core.banking_services.sovcombank.sovcombank_services. \
    sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot_validate import \
    FIELD_TYPES, FIELD_RANGES, FIELD_ENUMS, REQUIRED_FIELDS
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_service import endpoint_processor


# sovcombank_request_service = SovcombankRequestService()
# validate_service = CommonValidateFieldService()
#
# sovcombank_build_request_service = CommonBankBuildingRequestsService(
#     f'{BASE_DIR}/apps/core/banking_services/sovcombank/sovcombank_services/templates_json/sovcombank_shot.json')
#
# data = sovcombank_build_request_service.template_data
#


# data_request = sovcombank_build_request_service.fill_templates_request(
#     data,
#     **goods_info,
#     **application_info,
#     **source_system_info,
#     **credit_info,
#     **person_info
# )
#
# if validate_service.validate_fields(
#         data_request,
#         REQUIRED_FIELDS,
#         FIELD_TYPES,
#         FIELD_RANGES,
#         FIELD_ENUMS
# ):
#     # print(json.dumps(data_request, indent=4, ensure_ascii=False))
#     response = sovcombank_request_service.send_request(data_request)
#
#     if response.get('status_code') == 200:
#         result_shot = endpoint_processor.handle_endpoint_response("sovcombank_shot", response)
#         print(result_shot)
#     else:
#         raise ValueError(f"Ошибка при отправке запроса: {response.status_code}")
from apps.questionnaire.models import ClientPreData


class DataPreparationService:
    def __init__(self):
        self.sovcombank_build_request_service = CommonBankBuildingRequestsService(
            f'{BASE_DIR}/apps/core/banking_services/sovcombank/sovcombank_services/templates_json/sovcombank_shot.json')
        self.data = self.sovcombank_build_request_service.template_data

    def prepare_data(self, user, client_id):
        client = get_object_or_404(ClientPreData, pk=client_id)

        application_info = {
            "applicationInfo": {
                "partnerId": "НАШ ДИЛЕРСКИЙ ЦЕНТР#г Москва#Москва#29276#Воронова Елена Юрьевна"
            }
        }

        source_system_info = {
            "sourceSystemInfo": {
                "idSystem": "Некий id системы"
            }
        }

        credit_info = {
            "creditInfo": {
                "product": "Кредит на автомобиль",
                "period": "12",
                "limit": float(client.total_loan_amount)
            }
        }

        person_info = {
            "person": {
                "firstName": f"{client.client_person_data.first().first_name_client}",
                "lastName": f"{client.client_person_data.first().last_name_client}",
                "sex": f"{client.client_person_data.first().gender_choice_client}",
                "birthplace": "ИРКУТСКАЯ ОБЛ",
                "dob": f"{client.client_person_data.first().birth_date_client}",
                "factAddressSameAsRegistration": True,
                "primaryDocument": {
                    "docType": "Паспорт",
                    "docNumber": f"{client.passport_data.first().series_number_passport}".split(" ")[1],
                    "docSeries": f"{client.passport_data.first().series_number_passport}".split(" ")[0],
                    "issueOrg": f"{client.passport_data.first().issued_by_passport}",
                    "issueDate": f"{client.passport_data.first().issue_date_passport}",
                    "issueCode": f"{client.passport_data.first().division_code_passport}"
                },
                "registrationAddress": {
                    "countryName": "Россия",
                    "region": f"{client.client_person_data.first().registration_address_client}".split(",")[0],
                    "postCode": "123456"
                },
                "incomes": [{
                    "incomeType": "",
                    "incomeAmount": 0.0,
                }]
            }
        }

        goods_info = {
            "goods": [
                {
                    "goodCost": 100.0},
                {
                    "goodCost": 50.0
                }
            ]
        }
        return self.sovcombank_build_request_service.fill_templates_request(
            self.data,
            **application_info,
            **source_system_info,
            **credit_info,
            **person_info,
            **goods_info
        )


class ValidationService:
    def __init__(self):
        self.validate_service = CommonValidateFieldService()

    def validate(self, data_request):
        return self.validate_service.validate_fields(
            data_request,
            REQUIRED_FIELDS,
            FIELD_TYPES,
            FIELD_RANGES,
            FIELD_ENUMS
        )


class RequestService:
    def __init__(self):
        self.sovcombank_request_service = SovcombankRequestService()

    def send_data(self, data_request):
        response = self.sovcombank_request_service.send_request(data_request)
        if response.get('status_code') == 200:
            result_shot = endpoint_processor.handle_endpoint_response("sovcombank_shot", response)
            return result_shot
        else:
            raise ValueError(f"Ошибка при отправке запроса: {response.get('status_code')}")


class SovcombankHandler:
    def __init__(self):
        self.data_preparation_service = DataPreparationService()
        self.validation_service = ValidationService()
        self.request_service = RequestService()

    def handle(self, user, client_id):
        data_request = self.data_preparation_service.prepare_data(user, client_id)

        if self.validation_service.validate(data_request):
            return self.request_service.send_data(data_request)


# handler = SovcombankHandler()
# result = handler.handle()
# print(result)
