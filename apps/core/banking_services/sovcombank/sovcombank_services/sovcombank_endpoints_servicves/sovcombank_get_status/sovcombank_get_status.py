import logging
import time
import asyncio

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

    def polling_status(self, headers):
        print('начало опроса')
        timeout = 1200  # 20 минут
        interval = 60  # 1 минута
        elapsed_time = 0

        while elapsed_time < timeout:
            # Запрашиваем статус заявки
            response = self.sovcombank_request_service.send_request("GET", headers)
            status = response.get('status')
            comment = response.get('comment', '')

            if status == 'IN WORK':
                print("Ошибка. Свяжитесь с поддержкой банка по интеграциям")
                return response

            elif status == 'Ошибка создания заявки':
                print(f"Ошибка валидации данных: {comment}")

                return {"error": "Ошибка валидации", "comment": comment}

            elif status == 'Прерван':
                print(f"Процесс прерван оператором: {comment}")
                return {"error": "Процесс прерван оператором", "comment": comment}

            elif status == 'Отказ':
                print("Банк отказал в кредите.")
                return {"error": "Отказ", "comment": "Кредит отклонён"}

            elif status == 'Временный отказ':
                print(f"Временный отказ: {comment}")
                return {"error": "Временный отказ", "comment": comment}

            elif status == 'В работе' and not comment:
                print("Заявка на проверках. Продолжаем опрос.")
                time.sleep(interval)
                elapsed_time += interval
                continue

            elif status == 'Предварительная заявка одобрена':
                print("Заявка прошла первые проверки.")

                return response  # Успешное завершение

            time.sleep(interval)
            elapsed_time += interval

        return {"error": "Заявка не была одобрена в течение 20 минут"}

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
            try:
                response_or_error = self.polling_status(headers)
                print(f"response_or_error = {response_or_error} {__name__}")
                return response_or_error
            except ValueError as e:
                print('Ошибка обрабтки хендлера status')
                formatted_massage = error_message_formatter(e=e, operation_id=self.operation_id)
                logger.error(formatted_massage)
                return ValueError('Ошибка обрабтки хендлера status')
        except FileNotFoundError:
            raise
        except AttributeError:
            raise
        except ValueError:
            raise
        except Exception:
            raise
