from celery import shared_task
from django.contrib.sessions.models import Session
from django.core.cache import cache

from apps.common_services.kafka.consumer.runner import KafkaConsumerRunner
from log_storage.logging_servivce import handle_logger
from log_storage.logging_config import logger_info


@shared_task
def run_kafka_consumer():
    """
    Celery-задача для запуска всех Kafka-консюмеров.
    """

    handle_logger('Запуск всех Kafka Consumers через Celery', logger_info)
    runner = KafkaConsumerRunner()

    try:
        runner.run_all()  # Запускаем всех консюмеров
        handle_logger("Все Kafka Consumers успешно выполнены", logger_info)
    except Exception as e:
        handle_logger(f"Ошибка при выполнении Kafka Consumers: {str(e)}", logger_info)


@shared_task
def logout_all_users():
    Session.objects.all().delete()
    cache.clear()
    handle_logger('Successfully logged out all users', logger_info)
