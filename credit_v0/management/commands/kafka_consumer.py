import time

from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaException
import json

from credit_v0.services.common_servive import convert_str_list
from credit_v0.services.kafka.kafka_service import KafkaProducerService
from credit_v0.services.questionnaire.questionnaire_service import BankOfferService


class Command(BaseCommand):
    help = 'Consumes messages from Kafka and updates the database'
    kafka_service = KafkaProducerService('database')
    config = kafka_service.read_config()
    config['group.id'] = 'bank-offers-group'
    config['auto.offset.reset'] = 'earliest'

    def handle(self, *args, **kwargs):
        config = self.config

        consumer = Consumer(config)
        consumer.subscribe(['database'])

        try:
            while True:
                time.sleep(1)
                msg = consumer.poll(0.1)
                if msg is None:
                    continue
                if msg.error():
                    raise KafkaException(msg.error())

                # Проверка на пустое сообщение
                if not msg.value():
                    self.stdout.write(self.style.ERROR('Received an empty or None message'))
                    continue

                # Обработка сообщения
                try:
                    data = json.loads(msg.value().decode('utf-8'))
                    client_id = data.get('client_id')
                    offer_ids = data.get('selected_offers')
                    print('offer_ids consume', offer_ids)
                    offer_ids = convert_str_list(offer_ids)
                    BankOfferService.process_offers(client_id, offer_ids)

                except json.JSONDecodeError as e:
                    self.stdout.write(self.style.ERROR(f'Failed to decode JSON: {str(e)}'))

        except KeyboardInterrupt:
            pass
        finally:
            consumer.close()
