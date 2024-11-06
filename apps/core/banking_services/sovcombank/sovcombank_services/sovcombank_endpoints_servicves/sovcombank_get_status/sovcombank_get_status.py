import logging
import time
import asyncio

from celery.result import AsyncResult

from app_v0.settings import BASE_DIR
from apps.core.banking_services.bank_requests_service import \
    CommonBankBuildingDataRequestsService, CommonValidateFieldService, SovcombankRequestService
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot import \
    ShotDataPreparationService

from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_service import endpoint_processor
from apps.core.common_services.common_simple_service import error_message_formatter
from apps.core.common_services.event_sourcing_service import EventSourcingService
from apps.questionnaire.tasks import send_request_get_status_task

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
        self.sovcombank_request_service = SovcombankRequestService()

    def polling_status(self, application_id, headers=None):
        print('начало опроса')
        timeout = 1200  # 20 минут
        interval = 60  # 1 минута
        elapsed_time = 0

        while elapsed_time < timeout:
            # Запрашиваем статус заявки
            response = self.sovcombank_request_service.send_request("GET",
                                                                    "http://host.docker.internal:8080",
                                                                    f"api/v3/credit/application/auto/{application_id}/status",
                                                                    extra_headers=headers)
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

    def poll_task(self, task_id):
        task_result = AsyncResult(task_id)
        while task_result.state in ['PENDING', 'STARTED']:
            print(f"Текущий статус: {task_result.state}")
            time.sleep(5)  # Ожидаем 5 секунд перед следующим запросом
            task_result = AsyncResult(task_id)  # Обновляем состояние задачи

        if task_result.state == 'SUCCESS':
            print("Задача завершена:")
            return task_result.result
        elif task_result.state == 'FAILURE':
            print("Задача завершилась ошибкой:")
            return task_result.result

    def send_request_get_status(self, application_id, headers=None):
        sovcombank_request_service = SovcombankRequestService()
        response = sovcombank_request_service.send_request("GET",
                                                           "http://host.docker.internal:8080",
                                                           f"api/v3/credit/application/auto/{application_id}/status",
                                                           extra_headers=headers)
        print('запрос прошел----------------')

        return response

    def run_response_task(self, application_id):
        return send_request_get_status_task.apply_async(args=[application_id])

    def handle_response(self, application_id, task_id):
        response_or_error = self.poll_task(task_id)
        status = response_or_error.get('status')
        count_in_work = 0

        if status == 'IN WORK' and count_in_work < 2:
            self.run_response_task(application_id)
            count_in_work += 1
            print('count_in_work', count_in_work)

        return response_or_error

    def handle(self, user, client_id, application_id):
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
            try:
                task = self.run_response_task(application_id)
                task_id = task.id
                response_or_error = self.handle_response(application_id, task_id)

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
