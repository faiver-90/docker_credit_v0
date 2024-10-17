import logging

from app_v0.settings import BASE_DIR
from apps.core.banking_services.building_bank_requests_service import \
    CommonBankBuildingDataRequestsService, CommonValidateFieldService, SovcombankRequestService
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot import \
    ShotDataPreparationService

from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_service import endpoint_processor
from apps.core.common_services.common_simple_servive import error_message_formatter
from apps.core.common_services.event_sourcing_service import EventSourcingService

logger = logging.getLogger(__name__)


class SovcombankGetStatusSendHandler:
    """
    Обработчик для отправки данных в Sovcombank по заявкам клиентов.

    Этот класс собирает, валидирует и отправляет данные клиента в банк, а также записывает ивенты.
    """

    def __init__(self, operation_id=None):
        self.operation_id = operation_id
        # self.data_preparation_service = ShotDataPreparationService(self.operation_id)
        self.validation_service = CommonValidateFieldService(self.operation_id)
        self.event_sourcing_service = EventSourcingService()
        self.sovcombank_request_service = SovcombankRequestService("http://host.docker.internal:8080",
                                                                   "apy-key")

    def handle(self, user, client_id, applicationId):
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
            # data_request_not_converted = self.data_preparation_service.prepare_data(client_id,
            #                                                                         self.operation_id)
            # data_request_converted = self.data_preparation_service.convert_fields(data_request_not_converted,
            #                                                                       FIELD_TYPES_SHOT)

            # if self.validation_service.validate_fields(
            #         data_request_converted,
            #         REQUIRED_FIELDS_SHOT,
            #         FIELD_TYPES_SHOT,
            #         FIELD_RANGES_SHOT,
            #         FIELD_ENUMS_SHOT,
            # ):
            #     self.event_sourcing_service.record_event(
            #         user.id,
            #         'send_request_to_sovcombank_shot',
            #         data_request_converted,
            #         client_id=client_id)

            sovcombank_build_request_service = CommonBankBuildingDataRequestsService(self.operation_id)

            headers = self.sovcombank_request_service.building_request(
                f"/api/v3/credit/application/auto/{applicationId}/status")
            response = self.sovcombank_request_service.send_request("GET", headers)

            if response:
                try:
                    result_status = endpoint_processor.handle_endpoint_response("sovcombank_get_status", response)
                    print(result_status)
                except ValueError as e:
                    formatted_massage = error_message_formatter(e=e, operation_id=self.operation_id)
                    logger.error(formatted_massage)
                    raise
                return result_status
            else:
                print('Ошибка обрабтки хендлера status')
        except FileNotFoundError:
            raise
        except AttributeError:
            raise
        except ValueError as e:
            raise
        except Exception:
            raise
