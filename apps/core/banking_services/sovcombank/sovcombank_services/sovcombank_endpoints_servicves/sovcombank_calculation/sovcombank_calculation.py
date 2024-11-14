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

from apps.core.banking_services.sovcombank.sovcombank_services. \
    sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot_validate import \
    FIELD_TYPES_SHOT, FIELD_RANGES_SHOT, FIELD_ENUMS_SHOT, REQUIRED_FIELDS_SHOT
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_service import endpoint_processor
from apps.core.common_services.common_simple_service import convert_value, load_file, get_local_var_for_exception, \
    error_message_formatter, create_uuid
from apps.core.common_services.event_sourcing_service import EventSourcingService
from apps.core.models import OffersSovComBank
from apps.questionnaire.models import ClientPreData

logger = logging.getLogger(__name__)


class CalculatorDataPreparationService:
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

    def prepare_data(self, client_id, operation_id=None):
        try:
            client = get_object_or_404(ClientPreData, pk=client_id)
            # person_data = client.client_person_data.first()
            calculations = []

            try:
                request_id = str(uuid.uuid4())
                offers = OffersSovComBank.objects.all()
                dealer_id = ''
                credit_info = {
                    'period': 12,
                    'payment': 1444.87
                }
                vehicle_info = {
                    "type": "Новый",
                    "brand": "KAIYI",
                    "model": "X3 Pro",
                    "constructionYear": 2023
                }

                deal_cost = {
                    "amount": 2250000.88,
                    "currency": "810"
                }

                insurance_list = []

                # Текущая дата
                # current_date = datetime.now().strftime("%Y-%m-%d")
                for i, offer in enumerate(offers, start=1):
                    calculation_id = i
                    product = offer.id_in_excel_file_sovcom

                    calculation = {
                        "calculationId": f"{calculation_id}",
                        "creditInfo": {
                            "product": f"{product}",
                            "period": credit_info.get('period'),
                            "payment": credit_info.get('payment')
                        },
                        "vehicleInfo": {
                            "type": vehicle_info.get('type'),
                            "brand": vehicle_info.get('brand'),
                            "model": vehicle_info.get('model'),
                            "constructionYear": vehicle_info.get('constructionYear')
                        },
                        "dealCost": {
                            "amount": deal_cost.get('amount'),
                            "currency": deal_cost.get('currency')
                        },

                        # ===================
                        "insuranceList": [
                            {
                                "type": "КАСКО",
                                "period": 12,
                                "agreementPercent": 3.036,
                                "cost": {
                                    "amount": 44940.12,
                                    "currency": "810"
                                },
                                "paymentType": "ВКредит",
                                "company": {
                                    "type": "Банковская",
                                    "insurerId": "22"
                                }
                            }
                        ]
                    }

                request_data = {
                    "requestId": request_id,
                    "dealerId": dealer_id,
                    "calculations": calculations
                }
                calculations.append(request_data)

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

            data_from_file = self.get_data_from_file_template(self.path_to_template)
            # Возвращаем результат объединения данных с шаблоном
            return self.sovcombank_build_request_service.fill_templates_request(
                data_from_file,
                # **application_info,
                # **source_system_info,
                # **credit_info,
                # **person_info,
                # **goods_info
            )
        except FileNotFoundError as e:
            text_massage = error_message_formatter(e=e, operation_id=self.operation_id)
            logger.error(text_massage)
            raise FileNotFoundError(text_massage)
        except AttributeError:
            raise


class SovcombankCalculatorSendHandler:
    def __init__(self, operation_id=None):
        self.operation_id = operation_id
        self.data_preparation_service = CalculatorDataPreparationService(self.operation_id)
        self.validation_service = CommonValidateFieldService(self.operation_id)
        self.event_sourcing_service = EventSourcingService()
        self.sovcombank_request_service = SovcombankRequestService()

    def calculator_handle(self, user, client_id):
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
                    'send_request_to_sovcombank_calculation',
                    data_request_converted,
                    client_id=client_id)
                response = self.sovcombank_request_service.send_request(
                    "POST",
                    "http://host.docker.internal:8080",
                    "/api/v3/credit/application/auto/calculation",
                    data=data_request_converted
                )

                if response:
                    try:
                        result_calculator = endpoint_processor.handle_endpoint_response("sovcombank_calculation",
                                                                                        response)
                        print(result_calculator)
                    except ValueError as e:
                        formatted_massage = error_message_formatter(e=e,
                                                                    operation_id=self.operation_id)
                        logger.error(formatted_massage)
                        raise
                    return result_calculator
                else:
                    print('Ошибка обрабтки хендлера')
                    raise ValueError(f"Ошибка при отправке запроса: {response.get('status_code')}")
        except FileNotFoundError:
            raise
        except AttributeError:
            raise
        except ValueError:
            raise
        except Exception:
            raise
