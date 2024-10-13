from django.shortcuts import get_object_or_404

from app_v0.settings import BASE_DIR
from apps.core.banking_services.building_bank_requests_service import (
    CommonBankBuildingDataRequestsService,
    CommonValidateFieldService, SovcombankRequestService)

from apps.core.banking_services.sovcombank.sovcombank_services. \
    sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot_validate import \
    FIELD_TYPES, FIELD_RANGES, FIELD_ENUMS, REQUIRED_FIELDS
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_service import endpoint_processor
from apps.core.common_services.event_sourcing_service import EventSourcingService
from apps.questionnaire.models import ClientPreData


class ShotDataPreparationService:
    def __init__(self):
        self.sovcombank_build_request_service = CommonBankBuildingDataRequestsService(
            f'{BASE_DIR}/apps/core/banking_services/sovcombank/sovcombank_services/templates_json/sovcombank_shot.json')
        self.data = self.sovcombank_build_request_service.template_data

    def prepare_data(self, user, client_id):
        # Получаем клиента и сразу выбираем связанные данные
        client = get_object_or_404(ClientPreData.objects.prefetch_related(
            'client_person_data', 'passport_data', 'financial_info', 'car_info'
        ), pk=client_id)

        # Получаем первую запись из связанных данных (если они есть)
        person_data = client.client_person_data.first()
        passport_data = client.passport_data.first()
        financial_info = client.financial_info.first()
        car_info = client.car_info.first()
        citizenship = client.citizenship.first()
        financing_conditions = client.financing_conditions.first()

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
                "product": str(f"{client.product_pre_client}"),
                "period": str(f"{financing_conditions.financing_term}"),
                "limit": float(client.total_loan_amount)
            }
        }

        person_info = {
            "person": {
                "firstName": str(person_data.first_name_client if person_data else ""),
                "lastName": str(person_data.last_name_client if person_data else ""),
                "sex": str(person_data.gender_choice_client if person_data else ""),
                "birthplace": str(f"{citizenship.birth_place_citizenship}" if citizenship else ""),
                "dob": str(person_data.birth_date_client if person_data else ""),
                "factAddressSameAsRegistration": True,
                "primaryDocument": {
                    "docType": "Паспорт",
                    "docNumber": str(passport_data.series_number_passport.split(" ")[1] if passport_data else ""),
                    "docSeries": str(passport_data.series_number_passport.split(" ")[0] if passport_data else ""),
                    "issueOrg": str(passport_data.issued_by_passport if passport_data else ""),
                    "issueDate": str(passport_data.issue_date_passport if passport_data else ""),
                    "issueCode": str(passport_data.division_code_passport if passport_data else "")
                },
                "registrationAddress": {
                    "countryName": str(f"{person_data.country_name_pre_client}" if citizenship else ""),
                    "region": str(person_data.registration_address_client.split(",")[0] if person_data else ""),
                    "postCode": str(f"{person_data.post_code}" if person_data else "")
                },
                "incomes": [{
                    "incomeType": str(f"{financial_info.income_type}"  if financial_info else ""),
                    "incomeAmount": float(financial_info.income_amount) if person_data else 0,
                }]
            }
        }

        goods_info = {
            "goods": [
                {
                    "goodCost": car_info.car_price_car_info if car_info else 0
                }]
        }

        data_not_validate = self.sovcombank_build_request_service.fill_templates_request(
            self.data,
            **application_info,
            **source_system_info,
            **credit_info,
            **person_info,
            **goods_info
        )

        # ====== Удалить после конца формирования ========
        result = ValidationService().validate(data_not_validate)
        if result:
            return self.sovcombank_build_request_service.fill_templates_request(
                {},
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
            REQUIRED_FIELDS,
            FIELD_TYPES,
            FIELD_RANGES,
            FIELD_ENUMS
        )


class SovcombankShotSendHandler:
    def __init__(self):
        self.data_preparation_service = ShotDataPreparationService()
        self.validation_service = ValidationService()
        self.event_sourcing_service = EventSourcingService()
        self.sovcombank_request_service = SovcombankRequestService("base_url", "api_key")

    def handle(self, user, client_id):
        data_request = self.data_preparation_service.prepare_data(user, client_id)

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
