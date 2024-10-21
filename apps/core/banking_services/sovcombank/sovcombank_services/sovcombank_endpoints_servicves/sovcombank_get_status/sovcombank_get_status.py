import logging
import time

from app_v0.settings import BASE_DIR
from apps.core.banking_services.bank_requests_service import \
    CommonBankBuildingDataRequestsService, CommonValidateFieldService, SovcombankRequestService
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot import \
    ShotDataPreparationService

from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_service import endpoint_processor
from apps.core.common_services.common_simple_service import error_message_formatter
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

    def getting_good_status(self, headers):
        # Повторение запроса раз в 10 секунд до 20 минут (1200 секунд)
        timeout = 1200  # 20 минут
        interval = 60  # Интервал 10 секунд
        elapsed_time = 0
        while elapsed_time < timeout:
            # Отправляем запрос
            response = self.sovcombank_request_service.send_request("GET", headers)

            # Проверяем, есть ли нужный комментарий
            comment = response.get('status')
            if comment == 'Предварительная заявка одобрена':
                print("Заявка одобрена")
                break  # Выход из цикла при успешной проверке

            # elif comment == 'IN WORK':
            #     print("Ошибка на стороне АПИ. Повторите отправку")
            #     break

            time.sleep(interval)
            elapsed_time += interval
        else:
            raise ValueError('Заявка не была одобрена в течение 20 минут')
        return response

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
            headers = self.sovcombank_request_service.building_headers(
                f"/api/v3/credit/application/auto/{applicationId}/status")
            response = self.getting_good_status(headers)

            if response:
                try:
                    result_status = endpoint_processor.handle_endpoint_response("sovcombank_get_status", response)
                    print(result_status)

                    return result_status
                except ValueError as e:
                    formatted_massage = error_message_formatter(e=e, operation_id=self.operation_id)
                    logger.error(formatted_massage)
                    raise
            else:
                print('Ошибка обрабтки хендлера status')
                return ValueError('Ошибка обрабтки хендлера status')
        except FileNotFoundError:
            raise
        except AttributeError:
            raise
        except ValueError:
            raise
        except Exception:
            raise
