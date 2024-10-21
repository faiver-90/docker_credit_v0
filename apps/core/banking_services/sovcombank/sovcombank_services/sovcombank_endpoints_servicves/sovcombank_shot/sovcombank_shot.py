import logging
import uuid
from datetime import datetime

from django.db import connection
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from app_v0.settings import BASE_DIR
from apps.core.banking_services.bank_requests_service import (
    CommonBankBuildingDataRequestsService,
    CommonValidateFieldService, SovcombankRequestService)
from apps.core.banking_services.sovcombank.response_handler_factory import SovcombankEndpointResponseProcessor
from apps.core.banking_services.sovcombank.sovcombank_factory_response_handlers import SovcombankShotHandler

from apps.core.banking_services.sovcombank.sovcombank_services. \
    sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot_validate import \
    FIELD_TYPES_SHOT, FIELD_RANGES_SHOT, FIELD_ENUMS_SHOT, REQUIRED_FIELDS_SHOT
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_service import endpoint_processor
from apps.core.common_services.common_simple_service import convert_value, load_file, get_local_var_for_exception, \
    error_message_formatter
from apps.core.common_services.event_sourcing_service import EventSourcingService
from apps.questionnaire.models import ClientPreData

logger = logging.getLogger(__name__)


class ShotDataPreparationService:
    """
    Сервис для подготовки данных перед отправкой запроса в Sovcombank.

    Этот класс собирает данные клиента из БД и формирует их в нужном формате,
    а также выполняет конвертацию типов данных и полей.
    """

    def __init__(self, operation_id):
        self.operation_id = operation_id
        self.sovcombank_build_request_service = CommonBankBuildingDataRequestsService(operation_id=self.operation_id)
        self.name_modul = str(__name__).split(".")[-1]
        self.path_to_template = f'{BASE_DIR}/apps/core/banking_services/sovcombank/sovcombank_services/' \
                                f'templates_json/sovcombank_shot.json'

    def get_data_from_file_template(self, path_to_template):
        try:
            return load_file(path_to_template)
        except FileNotFoundError as e:
            massage = 'Файл не найден'
            formatted_massage = error_message_formatter(massage,
                                                        e=e,
                                                        module=self.name_modul,
                                                        path_to_template=path_to_template)
            raise FileNotFoundError(formatted_massage)

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

    def prepare_data(self, client_id, operation_id=None):
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
                region_registration = person_data.registration_address_client.split(",")[0]
                gender = self.convert_gender(str(person_data.gender_choice_client))
                current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            except AttributeError as e:
                local_var = get_local_var_for_exception()
                text_massage = 'Ошибка при обработке данных для клиента'
                formatted_message = error_message_formatter(text_massage,
                                                            e,
                                                            operation_id=operation_id,
                                                            client_id=client_id,
                                                            local_var=local_var)
                logger.error(formatted_message)
                raise AttributeError(formatted_message)

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
            data_from_file = self.get_data_from_file_template(self.path_to_template)
            # Возвращаем результат объединения данных с шаблоном
            return self.sovcombank_build_request_service.fill_templates_request(
                data_from_file,
                **application_info,
                **source_system_info,
                **credit_info,
                **person_info,
                **goods_info
            )
        except FileNotFoundError as e:
            text_massage = error_message_formatter(e=e, operation_id=self.operation_id)
            logger.error(text_massage)
            raise FileNotFoundError(text_massage)
        except AttributeError:
            raise


class SovcombankShotSendHandler:
    """
    Обработчик для отправки данных в Sovcombank по заявкам клиентов.

    Этот класс собирает, валидирует и отправляет данные клиента в банк, а также записывает ивенты.
    """

    def __init__(self, operation_id=None):
        self.operation_id = operation_id
        self.data_preparation_service = ShotDataPreparationService(self.operation_id)
        self.validation_service = CommonValidateFieldService(self.operation_id)
        self.event_sourcing_service = EventSourcingService()
        self.sovcombank_request_service = SovcombankRequestService("http://host.docker.internal:8080",
                                                                   "apy-key")

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

        try:
            data_request_not_converted = self.data_preparation_service.prepare_data(client_id,
                                                                                    self.operation_id)
            data_request_converted = self.data_preparation_service.convert_fields(data_request_not_converted,
                                                                                  FIELD_TYPES_SHOT)

            if self.validation_service.validate_fields(
                    data_request_converted,
                    REQUIRED_FIELDS_SHOT,
                    FIELD_TYPES_SHOT,
                    FIELD_RANGES_SHOT,
                    FIELD_ENUMS_SHOT,
            ):
                self.event_sourcing_service.record_event(
                    user.id,
                    'send_request_to_sovcombank_shot',
                    data_request_converted,
                    client_id=client_id)
                additional_headers = {
                    "Expected-Result": "success",
                }
                headers = self.sovcombank_request_service.building_headers("/api/v3/credit/application/auto/short",
                                                                           extra_headers=additional_headers)
                response = self.sovcombank_request_service.send_request(
                    "POST",
                    headers,
                    data_request_converted
                )

                if response:
                    try:
                        result_shot = endpoint_processor.handle_endpoint_response("sovcombank_shot", response)
                    except ValueError as e:
                        formatted_massage = error_message_formatter(e=e, operation_id=self.operation_id)
                        logger.error(formatted_massage)
                        raise
                    return result_shot
                else:
                    print('Ошибка обрабтки хендлера')
                    # raise ValueError(f"Ошибка при отправке запроса: {response.get('status_code')}")
        except FileNotFoundError:
            raise
        except AttributeError:
            raise
        except ValueError:
            raise
        except Exception:
            raise

# handler = SovcombankHandler()
# result = handler.handle()
# print(result)
