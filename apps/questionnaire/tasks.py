import logging

import requests
from billiard.exceptions import SoftTimeLimitExceeded
from celery import shared_task
from celery.exceptions import MaxRetriesExceededError
from django.contrib.sessions.models import Session
from django.core.cache import cache

# from apps.common_services.kafka.consumer.runner import KafkaConsumerRunner
# from apps.core.log_storage.logging_servivce import custom_logger
from apps.core.common_services.common_simple_service import error_message_formatter

logger = logging.getLogger(__name__)


# @shared_task
# def run_kafka_consumer():
#     """
#     Celery-задача для запуска всех Kafka-консюмеров.
#     """
#
#     handle_logger('Запуск всех Kafka Consumers через Celery', logger_info)
#     runner = KafkaConsumerRunner()
#
#     try:
#         runner.run_all()  # Запускаем всех консюмеров
#         handle_logger("Все Kafka Consumers успешно выполнены", logger_info)
#     except Exception as e:
#         handle_logger(f"Ошибка при выполнении Kafka Consumers: {str(e)}", logger_info)
#

@shared_task
def logout_all_users():
    Session.objects.all().delete()
    cache.clear()
    logger.info('Successfully logged out all users')


@shared_task(bind=True, soft_time_limit=60)
def send_request_get_status_task(self, application_id, headers=None, max_retries=20, retry_delay=60):
    from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_endpoints_servicves.sovcombank_get_status.sovcombank_get_status import \
        SovcombankGetStatusSendHandler
    if application_id is None:
        raise ValueError("application_id не передан в задачу")

    try:
        print('Запуск таски')
        handler = SovcombankGetStatusSendHandler()
        response = handler.send_request_get_status(application_id, headers)
        return response  # Успешный ответ завершает задачу


    except SoftTimeLimitExceeded as exc:
        logger.warning(f"Превышен soft time limit для application_id {application_id}. Попробуем повторно.")
        # Используем self.retry для перезапуска задачи после soft timeout
        try:
            raise self.retry(exc=exc, countdown=retry_delay, max_retries=max_retries)
        except MaxRetriesExceededError:
            logger.error(
                f"Задача не выполнена после максимального количества попыток для application_id {application_id}")
            return {'error': f"Задача не выполнена после максимального количества попыток для {application_id}"}
        except requests.exceptions.HTTPError as e:
            massage = error_message_formatter('HTTPError', e=e, application_id=application_id)
            logger.error(massage)

    except Exception as exc:
        try:
            logger.warning(f"Повторная попытка для application_id {application_id} после ошибки: {str(exc)}")
            # Используем self.retry для повторной попытки с задержкой
            raise self.retry(exc=exc, countdown=retry_delay, max_retries=max_retries)
        except MaxRetriesExceededError:
            logger.error(
                f"Задача не выполнена после максимального количества попыток для application_id {application_id}")
            return {'error': f"Задача не выполнена после максимального количества попыток для {application_id}"}
