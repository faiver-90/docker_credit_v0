from datetime import datetime

from django.shortcuts import get_object_or_404

from app_v0.settings import BASE_DIR
from apps.core.banking_services.building_bank_requests_service import (
    CommonBankBuildingDataRequestsService,
    CommonValidateFieldService, SovcombankRequestService)

from apps.core.banking_services.sovcombank.sovcombank_services. \
    sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot_validate import \
    FIELD_TYPES_SHOT, FIELD_RANGES_SHOT, FIELD_ENUMS_SHOT, REQUIRED_FIELDS_SHOT
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_service import endpoint_processor
from apps.core.common_services.common_simple_servive import convert_value
from apps.core.common_services.event_sourcing_service import EventSourcingService
from apps.questionnaire.models import ClientPreData


class ShotDataPreparationService:
    def __init__(self):
        self.sovcombank_build_request_service = CommonBankBuildingDataRequestsService(
            f'{BASE_DIR}/apps/core/banking_services/sovcombank/sovcombank_services/templates_json/sovcombank_shot.json')
        self.data = self.sovcombank_build_request_service.template_data

    def prepare_data(self, client_id):
        # Получаем клиента и сразу выбираем связанные данные
        client = get_object_or_404(ClientPreData, pk=client_id)

        # Получаем первую запись из связанных данных (если они есть)
        person_data = client.client_person_data.first()
        passport_data = client.passport_data.first()
        financial_info = client.financial_info.first()
        car_info = client.car_info.first()
        citizenship = client.citizenship.first()
        financing_conditions = client.financing_conditions.first()
        passport_series_from_db = passport_data.series_number_passport.split(" ")[0]
        passport_series = passport_series_from_db[:2] + " " + passport_series_from_db[2:]
        passport_number = passport_data.series_number_passport.split(" ")[1]
        region_registration = person_data.registration_address_client.split(",")[0]
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        application_info = {
            "applicationInfo": {
                "partnerId": "ООО Обухов Автоцентр#Москва#Москва#15703#testalfa_Sovcom testalfa_Sovcom#6470",
                "type": "short",
                "dateSendWeb": convert_value(current_date, str)
            }
        }

        source_system_info = {
            "sourceSystemInfo": {
                "idSystem": "astPlatform"
            }
        }

        credit_info = {
            "creditInfo": {
                "product": "номер продукта в системе банка",
                "period": convert_value(financing_conditions.financing_term, str),
                "limit": convert_value(client.total_loan_amount, float)
            }
        }

        person_info = {
            "person": {
                "firstName": convert_value(person_data.first_name_client, str),
                "lastName": convert_value(person_data.last_name_client, str),
                "middleName": convert_value(person_data.middle_name_client, str),
                "sex": convert_value(person_data.gender_choice_client, str),
                "birthplace": convert_value(citizenship.birth_place_citizenship, str),
                "dob": convert_value(person_data.birth_date_client, str),
                "factAddressSameAsRegistration": True,
                "primaryDocument": {
                    "docType": convert_value("Паспорт", str),
                    "docNumber": convert_value(passport_number, str),
                    "docSeries": convert_value(passport_series, str),
                    "issueOrg": convert_value(passport_data.issued_by_passport, str),
                    "issueDate": convert_value(passport_data.issue_date_passport, str),
                    "issueCode": convert_value(passport_data.division_code_passport, str)
                },
                "registrationAddress": {
                    "countryName": convert_value(person_data.country_name_pre_client, str),
                    "region": convert_value(region_registration, str),
                    "postCode": convert_value(person_data.post_code, str)
                },
                "incomes": [{
                    "incomeType": convert_value(financial_info.income_type, str),
                    "incomeAmount": convert_value(financial_info.income_amount, float)
                }]
            }
        }

        goods_info = {
            "goods": [
                {
                    "goodCost": convert_value(car_info.car_price_car_info, float),
                    "goodModel": "",
                    "goodsDescription": "",
                    "goodType": ""
                }
            ]
        }

        # ====== Удалить после конца формирования ========
        data_not_validate = self.sovcombank_build_request_service.fill_templates_request(
            self.data,
            **application_info,
            **source_system_info,
            **credit_info,
            **person_info,
            **goods_info
        )

        result = ValidationService().validate(data_not_validate)
        if result:
            return self.sovcombank_build_request_service.fill_templates_request(
                self.data,
                **application_info,
                **source_system_info,
                **credit_info,
                **person_info,
                **goods_info
            )
        else:
            return 'Не прошло валидацию'
        # ======================================

        # Возвращаем результат объединения данных с шаблоном
        # return self.sovcombank_build_request_service.fill_templates_request(
        #     self.data,
        #     **application_info,
        #     **source_system_info,
        #     **credit_info,
        #     **person_info,
        #     **goods_info
        # )


class ValidationService:
    def __init__(self):
        self.validate_service = CommonValidateFieldService()

    def validate(self, data_request):
        return self.validate_service.validate_fields(
            data_request,
            REQUIRED_FIELDS_SHOT,
            FIELD_TYPES_SHOT,
            FIELD_RANGES_SHOT,
            FIELD_ENUMS_SHOT
        )


class SovcombankShotSendHandler:
    def __init__(self):
        self.data_preparation_service = ShotDataPreparationService()
        self.validation_service = ValidationService()
        self.event_sourcing_service = EventSourcingService()
        self.sovcombank_request_service = SovcombankRequestService("base_url", "api_key")

    def handle(self, user, client_id):
        data_request = self.data_preparation_service.prepare_data(client_id)

        if self.validation_service.validate(data_request):
            self.event_sourcing_service.record_event(user.id,
                                                     'send_request_to_sovcombank_shot',
                                                     data_request,
                                                     client_id=client_id)

            self.sovcombank_request_service.building_request("api/v3/credit/application/auto/short")
            response = self.sovcombank_request_service.send_request(
                "POST",
                data_request
            )

            if response.get('status_code') == 200:
                result_shot = endpoint_processor.handle_endpoint_response("sovcombank_shot", response)
                return result_shot
            else:
                raise ValueError(f"Ошибка при отправке запроса: {response.get('status_code')}")

# handler = SovcombankHandler()
# result = handler.handle()
# print(result)
