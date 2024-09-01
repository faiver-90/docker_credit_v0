import logging


from celery import shared_task
from credit_v0.services.kafka.consumer.runner import KafkaConsumerRunner

logger_info = logging.getLogger('info').info


@shared_task
def i():
    print("Starting infinite logging task")


@shared_task
def run_kafka_consumer():
    """
    Celery-задача для запуска всех Kafka-консюмеров.
    """

    logger_info('Запуск всех Kafka Consumers через Celery"')
    runner = KafkaConsumerRunner()

    try:
        runner.run_all()  # Запускаем всех консюмеров
        logger_info("Все Kafka Consumers успешно выполнены")
    except Exception as e:
        logger_info(f"Ошибка при выполнении Kafka Consumers: {str(e)}")
