import logging
from datetime import datetime

from django.db import connection
from django.http import JsonResponse
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

logger = logging.getLogger(__name__)


class ShotDataPreparationService:
    """
    Сервис для подготовки данных перед отправкой запроса в Sovcombank.

    Этот класс собирает данные клиента из БД и формирует их в нужном формате,
    а также выполняет конвертацию типов данных и полей.
    """

    def __init__(self):
        self.sovcombank_build_request_service = CommonBankBuildingDataRequestsService(
            f'{BASE_DIR}/apps/core/banking_services/sovcombank/sovcombank_services/templates_json/sovcombank_shot.json')
        self.data = self.sovcombank_build_request_service.template_data

    @staticmethod
    def convert_fields(data, field_types):
        """
        Конвертирует поля данных в указанные типы.

        Параметры:
        -----------
        data : dict
            Данные для конвертации.

        field_types : dict
            Ожидаемые типы полей для конвертации.

        Возвращает:
        -----------
        dict
            Обновленные данные с конвертированными полями.
        """

        for field, expected_type in field_types.items():
            keys = field.split('.')
            temp = data
            for key in keys[:-1]:
                if isinstance(temp, dict) and key in temp:
                    temp = temp[key]
                else:
                    break
            else:
                if isinstance(temp.get(keys[-1]), expected_type):
                    continue
                temp[keys[-1]] = convert_value(temp.get(keys[-1]), expected_type)
        return data

    @staticmethod
    def convert_gender(gender):
        """
        Конвертирует пол клиента из текстового значения в сокращенное буквенное представление.

        Параметры:
        -----------
        gender : str
            Пол клиента ('Муж' или 'Жен').

        Возвращает:
        -----------
        str
            Сокращенное представление пола ('m' или 'f').
        """
        if gender == 'Муж':
            return 'm'
        elif gender == 'Жен':
            return 'f'
        else:
            return 'Недопустимое значение'

    def prepare_data(self, client_id):
        """
        Подготавливает данные клиента для отправки в банк, включая информацию о кредите,
        персональные данные и данные о товаре.

        Параметры:
        -----------
        client_id : int
            ID клиента, чьи данные нужно подготовить.

        Возвращает:
        -----------
        dict
            Подготовленные данные клиента для отправки.
        """
        try:
            # Получаем клиента и связанные данные
            client = get_object_or_404(ClientPreData, pk=client_id)
            person_data = client.client_person_data.first()
            passport_data = client.passport_data.first()
            financial_info = client.financial_info.first()
            car_info = client.car_info.first()
            financing_conditions = client.financing_conditions.first()
            try:
                passport_series_from_db = passport_data.series_number_passport.split(" ")[0]
                passport_series = passport_series_from_db[:2] + " " + passport_series_from_db[2:]
                passport_number = passport_data.series_number_passport.split(" ")[1]
            except AttributeError as e:
                logger.error(f"Ошибка при обработке паспортных данных для клиента {client_id}: {str(e)}")
                raise ValueError(f"Ошибка в паспортных данных для клиента {client_id}: {str(e)}")
            except IndexError as e:
                logger.error(f"Ошибка в формате паспортных данных для клиента {client_id}: {str(e)}")
                raise ValueError(f"Неправильный формат паспортных данных для клиента {client_id}: {str(e)}")

            # Обрабатываем данные регистрации
            try:
                region_registration = person_data.registration_address_client.split(",")[0]
            except AttributeError as e:
                logger.error(f"Ошибка при обработке адреса регистрации для клиента {client_id}: {str(e)}")
                raise ValueError(f"Ошибка в данных регистрации клиента {client_id}: {str(e)}")

            # Конвертируем пол
            try:
                gender = self.convert_gender(str(person_data.gender_choice_client))
            except Exception as e:
                logger.error(f"Ошибка при конвертации пола для клиента {client_id}: {str(e)}")
                raise ValueError(f"Ошибка при обработке данных о поле клиента {client_id}: {str(e)}")

            current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Формируем данные для запроса
            application_info = {
                "applicationInfo": {
                    "partnerId": "ООО Обухов Автоцентр#Москва#Москва#15703#testalfa_Sovcom testalfa_Sovcom#6470",
                    "type": "short",
                    "dateSendWeb": current_date
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
                    "period": financing_conditions.financing_term,
                    "limit": client.total_loan_amount,
                }
            }

            person_info = {
                "person": {
                    "firstName": person_data.first_name_client,
                    "lastName": person_data.last_name_client,
                    "middleName": person_data.middle_name_client,
                    "sex": gender,
                    "birthplace": person_data.birth_place_citizenship,
                    "dob": person_data.birth_date_client,
                    "factAddressSameAsRegistration": person_data.fact_address_same_registration,
                    "primaryDocument": {
                        "docType": "Паспорт",
                        "docNumber": passport_number,
                        "docSeries": passport_series,
                        "issueOrg": passport_data.issued_by_passport,
                        "issueDate": passport_data.issue_date_passport,
                        "issueCode": passport_data.division_code_passport
                    },
                    "registrationAddress": {
                        "countryName": person_data.country_name_pre_client,
                        "region": region_registration,
                        "postCode": person_data.post_code
                    },
                    "incomes": [{
                        "incomeType": str(financial_info.income_type),
                        "incomeAmount": float(financial_info.income_amount)
                    }]
                }
            }

            goods_info = {
                "goods": [
                    {
                        "goodCost": car_info.car_price_car_info,
                        "goodModel": "",
                        "goodsDescription": "",
                        "goodType": ""
                    }
                ]
            }

            # Сборка данных для валидации
            data_not_validate = self.sovcombank_build_request_service.fill_templates_request(
                self.data,
                **application_info,
                **source_system_info,
                **credit_info,
                **person_info,
                **goods_info
            )

            converted_data = self.convert_fields(data_not_validate, FIELD_TYPES_SHOT)

            # Валидация данных
            result = ValidationService().validate(converted_data)

            if result:
                return converted_data
            else:
                raise ValueError("Validation failed")


        except AttributeError as e:
            logger.error(f"Ошибка данных для клиента {client_id}: {str(e)}")
            raise ValueError(f"Ошибка данных для клиента {client_id}: {str(e)}")

        except Exception as e:
            logger.error(f"Неизвестная ошибка при подготовке данных для клиента {client_id}: {str(e)}")
            raise ValueError(f"Неизвестная ошибка при подготовке данных для клиента {client_id}: {str(e)}")
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
    """
    Сервис для валидации данных перед отправкой запроса в Sovcombank.

    Этот класс проверяет наличие обязательных полей, корректные типы данных,
    а также диапазоны и допустимые значения для полей.
    """

    def __init__(self):
        self.validate_service = CommonValidateFieldService()

    def validate(self, data_request):
        """
        Валидирует данные запроса, проверяя обязательные поля, типы данных и диапазоны.

        Параметры:
        -----------
        data_request : dict
           Данные для валидации.

        Возвращает:
        -----------
        bool
           True, если данные прошли валидацию, иначе выбрасывается исключение.
        """
        return self.validate_service.validate_fields(
            data_request,
            REQUIRED_FIELDS_SHOT,
            FIELD_TYPES_SHOT,
            FIELD_RANGES_SHOT,
            FIELD_ENUMS_SHOT
        )


class SovcombankShotSendHandler:
    """
    Обработчик для отправки данных в Sovcombank по заявкам клиентов.

    Этот класс собирает, валидирует и отправляет данные клиента в банк, а также записывает ивенты.
    """

    def __init__(self):
        self.data_preparation_service = ShotDataPreparationService()
        self.validation_service = ValidationService()
        self.event_sourcing_service = EventSourcingService()
        self.sovcombank_request_service = SovcombankRequestService("base_url", "api_key")

    def handle(self, user, client_id):
        """
        Выполняет полный цикл отправки данных в Sovcombank.

        Параметры:
        -----------
        user : User
            Пользователь, выполняющий действие.

        client_id : int
            ID клиента, чьи данные нужно отправить.

        Возвращает:
        -----------
        dict
            Результат обработки ответа от банка.
        """
        data_request_not_converted = self.data_preparation_service.prepare_data(client_id)
        data_request_converted = self.data_preparation_service.convert_fields(data_request_not_converted,
                                                                              FIELD_TYPES_SHOT)

        if self.validation_service.validate(data_request_converted):
            self.event_sourcing_service.record_event(user.id,
                                                     'send_request_to_sovcombank_shot',
                                                     data_request_converted,
                                                     client_id=client_id)

            self.sovcombank_request_service.building_request("api/v3/credit/application/auto/short")
            response = self.sovcombank_request_service.send_request(
                "POST",
                data_request_converted
            )

            if response.get('status_code') == 200:
                result_shot = endpoint_processor.handle_endpoint_response("sovcombank_shot", response)
                return result_shot
            else:
                raise ValueError(f"Ошибка при отправке запроса: {response.get('status_code')}")

# handler = SovcombankHandler()
# result = handler.handle()
# print(result)
