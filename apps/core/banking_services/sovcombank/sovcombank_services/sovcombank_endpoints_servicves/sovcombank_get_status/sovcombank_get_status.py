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
            'IN WORK': 'Необходимо связаться с поддержкой банка по интеграциям',
            'Отказ': 'Банк принял решение о невозможности выдать кредит этому клиенту на таких условиях',
            'Временный отказ': 'Банк вернул заявку на доработку. Проверьте комментарий банка',
            'В работе': 'Статус в работе'
        }

    def send_request_get_status(self, application_id_bank, headers=None):
        try:
            logger.info(f"Отправка запроса на получение статуса для заявки {application_id_bank}")
            return self.sovcombank_request_service.send_request(
                "GET",
                "http://host.docker.internal:8080",
                f"api/v3/credit/application/auto/{application_id_bank}/status",
                extra_headers=headers
            )
        except Exception as e:
            logger.error(f"Ошибка при отправке запроса статуса для {application_id_bank}: {str(e)}")
            raise

    def start_status_request_task(self, application_id_in_bank, max_retries, retry_delay):
        try:
            logger.info(f"Запуск Celery задачи для получения статуса по заявке {application_id_in_bank}")
            return send_request_get_status_task.apply_async(args=[application_id_in_bank],
                                                            kwargs={'max_retries': max_retries,
                                                                    'retry_delay': retry_delay})
        except Exception as e:
            logger.error(f"Ошибка запуска Celery задачи для {application_id_in_bank}: {str(e)}")
            raise

    def handle_in_work_status(self, user, client_id, application_id_bank):
        """
        Обрабатывает статус 'IN WORK', выполняя повторные попытки запроса статуса.
        """
        attempt = 0
        max_attempts = 1
        delay = 5

        while attempt < max_attempts:
            logger.info(f"Попытка {attempt + 1} для статуса 'IN WORK' по заявке {application_id_bank}")
            try:
                sovcombank_handler = SovcombankShotSendHandler(operation_id=self.operation_id)
                response_shot_info = sovcombank_handler.short_handle(user, client_id)
                application_id_bank = response_shot_info.get('requestId', '')

                task = self.start_status_request_task(application_id_bank, max_retries=20, retry_delay=60)
                response_or_error = poll_task(task.id)
                status = response_or_error.get('status')

                if status != 'IN WORK':
                    return response_or_error

            except Exception as e:
                logger.error(f"Ошибка при обработке статуса 'IN WORK' для заявки {application_id_bank}: {str(e)}")
                raise

            attempt += 1
            time.sleep(delay)

        logger.warning(
            f"Достигнуто максимальное количество попыток для статуса 'IN WORK' по заявке {application_id_bank}")

        return {'description': 'Необходимо связаться с поддержкой банка по интеграциям.',
                'status': 'IN WORK'
                }

    def handle_in_hand(self, application_id_in_bank, status):
        try:
            response_or_error = None
            max_retries = 20
            retry_delay = 60
            accumulator = 0
            while status == 'В работе' or status == 'Прерван':
                if status == 'В работе':
                    max_retries = 20
                    retry_delay = 60
                elif status == 'Прерван':
                    max_retries = 20
                    retry_delay = 3600

                logger.info(
                    f"Запуск задачи для статуса '{status}' с {max_retries} попытками и задержкой {retry_delay} секунд")

                task = self.start_status_request_task(application_id_in_bank, max_retries=max_retries,
                                                      retry_delay=retry_delay)
                response_or_error = poll_task(task.id)
                status = response_or_error.get('status')

                # Ждём перед следующей попыткой, если статус не изменился
                if status == 'В работе' or status == 'Прерван':
                    time.sleep(retry_delay)
                    accumulator += 1
                    if accumulator > max_retries:
                        logger.warning(f"Достигнуто максимальное количество попыток для статуса '{status}' "
                                       f"по заявке {application_id_in_bank}. Задача завершена.")
                        return {'error': f"Превышено максимальное количество попыток для статуса '{status}'",
                                'status': status}


            return response_or_error
        except Exception as e:
            logger.error(
                f"Ошибка при обработке статуса 'В работе' или 'Прерван' для заявки {application_id_in_bank}: {str(e)}")
            raise

    def formatted_description(self, status, message_text=None, comment=None, **kwargs):
        additional_info = "<br>".join([f"{key} - {value}" for key, value in kwargs.items()])

        # Включаем дополнительные параметры в итоговое описание
        return f"description - {self.description_list.get(status, '')},<br>" \
               f"comment - {comment},<br>" \
               f"message_text - {message_text},<br>" \
               f"operation id - {self.operation_id},<br>" \
               f"{additional_info}"

    def handle(self, user, client_id, application_id_bank):
        """
        Основной метод для обработки и отправки данных в Sovcombank.
        """
        try:
            logger.info(f"Начало обработки заявки {application_id_bank}")
            task = self.start_status_request_task(application_id_bank, max_retries=20, retry_delay=60)
            response_or_error = poll_task(task.id)
            status = response_or_error.get('status')
            comment = response_or_error.get('comment', '')
            message_text = response_or_error.get('messageText', '')

            while status == 'В работе' or status == 'Прерван':
                time.sleep(5)
                response_or_error = self.handle_in_hand(application_id_bank, status)
                logger.debug(f"Промежуточный ответ: {response_or_error}")
                status = response_or_error.get('status', '')

            if status == 'IN WORK':
                response_or_error = self.handle_in_work_status(user, client_id, application_id_bank)

                status = response_or_error.get('status', '')
                comment = response_or_error.get('comment', '')
                message_text = response_or_error.get('messageText', '')
                response_or_error['description'] = self.formatted_description(status, message_text, comment)

            elif status in self.description_list:
                response_or_error['description'] = self.formatted_description(status, message_text, comment)
            else:
                massage = error_message_formatter('Неизвестный статус',
                                                  application_id_bank=application_id_bank,
                                                  user=user,
                                                  client_id=client_id,
                                                  operation_id=self.operation_id
                                                  )
                logger.exception(massage)
                response_or_error['description'] = self.formatted_description(status,
                                                                              message_text,
                                                                              comment,
                                                                              massage=massage )
            logger.info(f"Статус обработки для заявки {application_id_bank}: {status}")
            return status, response_or_error
        except ValueError as e:
            formatted_message = error_message_formatter(e=e, operation_id=self.operation_id)
            logger.exception(formatted_message)
            raise ValueError('Ошибка обработки статуса.') from e
        except (FileNotFoundError, AttributeError) as e:
            logger.exception(f"Специфическая ошибка: {e}")
            raise
        except Exception as e:
            logger.exception(f"Неизвестная ошибка: {e}, operation_id: {self.operation_id}")
            raise
