import logging


from celery import shared_task
from credit_v0.services.kafka.consumer.runner import KafkaConsumerRunner

logger = logging.getLogger('credit_v0')


@shared_task
def i():
    print("Starting infinite logging task")


@shared_task
def run_kafka_consumer():
    """
    Celery-задача для запуска всех Kafka-консюмеров.
    """
    logger.debug('Запуск всех Kafka Consumers через Celery"')
    print("Запуск всех Kafka Consumers через Celery")
    runner = KafkaConsumerRunner()

    try:
        runner.run_all()  # Запускаем всех консюмеров
        print("Все Kafka Consumers успешно выполнены")
    except Exception as e:
        print(f"Ошибка при выполнении Kafka Consumers: {str(e)}")
