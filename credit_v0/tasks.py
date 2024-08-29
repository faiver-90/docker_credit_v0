import logging
import time

from celery import Celery, shared_task
from app_v0.celery import celery_app
from credit_v0.services.kafka.consumer.runner import KafkaConsumerRunner

# from confluent_kafka import Consumer, KafkaException


# from credit_v0.tasks import run_kafka_consumer
# run_kafka_consumer.delay()

logger = logging.getLogger('credit_v0')

@shared_task
def i():
    print("Starting infinite logging task")
