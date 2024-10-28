import logging

from celery import shared_task
from django.contrib.sessions.models import Session
from django.core.cache import cache

# from apps.common_services.kafka.consumer.runner import KafkaConsumerRunner
# from apps.core.log_storage.logging_servivce import custom_logger

logger = logging.getLogger('users_file')
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
    logger.info('Successfully logged out all users', 'info')
