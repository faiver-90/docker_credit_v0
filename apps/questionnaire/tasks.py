import logging

from celery import shared_task
from django.contrib.sessions.models import Session
from django.core.cache import cache

# from apps.common_services.kafka.consumer.runner import KafkaConsumerRunner
# from apps.core.log_storage.logging_servivce import custom_logger


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


@shared_task
def send_request_get_status_task(application_id, headers=None):
    from apps.core.banking_services.sovcombank.sovcombank_services.sovcombank_endpoints_servicves.sovcombank_get_status.sovcombank_get_status import \
        SovcombankGetStatusSendHandler
    if application_id is None:
        raise ValueError("application_id не передан в задачу")
    handler = SovcombankGetStatusSendHandler()
    response = handler.send_request_get_status(application_id, headers)

    return response
