# services_kafka/consumer.py
import json

from credit_v0.services.common_servive import convert_str_list
from credit_v0.services.kafka.consumer.base_consumer import BaseKafkaConsumerService
from credit_v0.services.kafka.kafka_service import KafkaProducerService
from credit_v0.services.questionnaire.questionnaire_service import BankOfferService


class KafkaConsumerAddSelectedOfferIdService(BaseKafkaConsumerService):
    """
    Консюмер Kafka, который обрабатывает сообщения, добавляя идентификаторы выбранных предложений.
    """

    def __init__(self, topic, group_id='bank-offers-group'):
        kafka_service = KafkaProducerService()
        kafka_config = kafka_service.read_config()
        super().__init__(topic, group_id, kafka_config)

    def process_message(self, msg):
        try:
            data = json.loads(msg.value().decode('utf-8'))
            client_id = data.get('client_id')
            offer_ids = data.get('selected_offers')
            print('offer_ids consume', offer_ids)
            offer_ids = convert_str_list(offer_ids)
            print('offer_ids converted')
            BankOfferService.process_offers(client_id, offer_ids)
            print('BankOfferService worked')
        except json.JSONDecodeError as e:
            print(f'Failed to decode JSON: {str(e)}')
