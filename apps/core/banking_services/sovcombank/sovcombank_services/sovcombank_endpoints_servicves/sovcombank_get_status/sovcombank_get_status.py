import logging
import time

from apps.core.banking_services.bank_requests_service import CommonValidateFieldService, SovcombankRequestService
from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_endpoints_servicves.sovcombank_shot.sovcombank_shot import \
    SovcombankShotSendHandler
from apps.core.common_services.common_simple_service import error_message_formatter, poll_task
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

    def send_request_get_status(self, application_id_bank, headers=None):
        sovcombank_request_service = SovcombankRequestService()
        response = sovcombank_request_service.send_request("GET",
                                                           "http://host.docker.internal:8080",
                                                           f"api/v3/credit/application/auto/{application_id_bank}/status",
                                                           extra_headers=headers)
        return response

    def run_request_task(self, application_id_in_bank):
        return send_request_get_status_task.apply_async(args=[application_id_in_bank])

    def handle_status_response(self, application_id_in_bank, task_id):
        response_or_error = poll_task(task_id)
        print(f"response_or_error = {response_or_error} {__name__}")
        status = response_or_error.get('status')
        count_in_work = 0

        description = None
        if status == 'Предварительная заявка одобрена':
            description = 'Предварительная заявка одобрена, статус из handle_status_response'
            status = 'Предварительная заявка одобрена'

        if status == 'IN WORK':
            count_in_work += 1
        if status == 'IN WORK' and count_in_work == 1:
            status, description = 'IN WORK', 'Обратитесь в службу интеграций банка'

        return status, description

    def handle(self, user, client_id, application_id_bank, operation_id=None):
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
                task = self.run_request_task(application_id_bank)
                task_id = task.id
                status, description = self.handle_status_response(application_id_bank, task_id)
                if status == 'IN WORK':
                    sovcombank_handler = SovcombankShotSendHandler(operation_id=operation_id)
                    response_shot_info = sovcombank_handler.short_handle(user, client_id)
                    application_id_bank = response_shot_info.get('requestId', '')
                    task = self.run_request_task(application_id_bank)
                    task_id = task.id
                    status, description = self.handle_status_response(application_id_bank, task_id)

                return status, description
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
