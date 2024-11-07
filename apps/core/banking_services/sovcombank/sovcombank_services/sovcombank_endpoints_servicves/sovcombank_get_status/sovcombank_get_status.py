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
    """

    def __init__(self, operation_id=None):
        self.operation_id = operation_id
        self.validation_service = CommonValidateFieldService(self.operation_id)
        self.event_sourcing_service = EventSourcingService()
        self.sovcombank_request_service = SovcombankRequestService()
        self.description_list = {
            'Предварительная заявка одобрена': 'Предварительная заявка одобрена, можно запускать дальше.',
            'Ошибка создания заявки': 'Ошибка создания заявки, ознакомьтесь с деталями.',
            'Прерван': 'Переведено в ручное управление на стороне банка.',
            'IN WORK': 'Необходимо связаться с поддержкой банка по интеграциям'
        }
    def send_request_get_status(self, application_id_bank, headers=None):
        return self.sovcombank_request_service.send_request(
            "GET",
            "http://host.docker.internal:8080",
            f"api/v3/credit/application/auto/{application_id_bank}/status",
            extra_headers=headers
        )

    def start_status_request_task(self, application_id_in_bank):
        return send_request_get_status_task.apply_async(args=[application_id_in_bank])

    def handle_in_work_status(self, user, client_id, application_id_bank):
        """
        Обрабатывает статус 'IN WORK', выполняя повторные попытки запроса статуса.
        """
        attempt = 0
        max_attempts = 1
        delay = 5

        while attempt < max_attempts:
            logger.info(f"Попытка {attempt + 1} для статуса 'IN WORK' по заявке {application_id_bank}")
            sovcombank_handler = SovcombankShotSendHandler(operation_id=self.operation_id)
            response_shot_info = sovcombank_handler.short_handle(user, client_id)
            application_id_bank = response_shot_info.get('requestId', '')

            task = self.start_status_request_task(application_id_bank)
            response_or_error = poll_task(task.id)
            status = response_or_error.get('status')

            if status != 'IN WORK':
                return status, response_or_error

            attempt += 1
            time.sleep(delay)

        logger.warning(
            f"Достигнуто максимальное количество попыток для статуса 'IN WORK' по заявке {application_id_bank}")

        return 'IN WORK', {'description': 'Необходимо связаться с поддержкой банка по интеграциям.'}

    def formatted_description(self, status, message_text=None, comment=None):
        return f"description - {self.description_list.get(status, '')},<br>" \
               f"comment - {comment},<br>" \
               f"message_text - {message_text}"

    def handle(self, user, client_id, application_id_bank):
        """
        Основной метод для обработки и отправки данных в Sovcombank.
        """

        try:
            task = self.start_status_request_task(application_id_bank)
            response_or_error = poll_task(task.id)
            status = response_or_error.get('status')
            comment = response_or_error.get('comment', '')
            message_text = response_or_error.get('messageText', '')
            if status == 'IN WORK':
                status, response_or_error = self.handle_in_work_status(user, client_id, application_id_bank)
                comment = response_or_error.get('comment', '')
                message_text = response_or_error.get('messageText', '')
                response_or_error['description'] = self.formatted_description(status, message_text, comment)
            elif status == 'Предварительная заявка одобрена':
                response_or_error['description'] = self.formatted_description(status, message_text, comment)
            elif status == 'Ошибка создания заявки':
                response_or_error['description'] = self.formatted_description(status, message_text, comment)
            elif status == 'Прерван':
                response_or_error['description'] =self.formatted_description(status, message_text, comment)
            return status, response_or_error


        except ValueError as e:
            formatted_message = error_message_formatter(e=e, operation_id=self.operation_id)
            logger.error(formatted_message)
            raise ValueError('Ошибка обработки статуса.') from e
        except (FileNotFoundError, AttributeError) as e:
            logger.exception(f"Специфическая ошибка: {e}")
            raise
        except Exception as e:
            logger.error(f"Неизвестная ошибка: {e}, operation_id: {self.operation_id}")
            raise
