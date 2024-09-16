import json

from apps.common_services.kafka.consumer.base_consumer import BaseKafkaConsumerService
from apps.common_services.kafka.kafka_service import KafkaProducerService
from apps.questionnaire.services.common_servive import convert_str_list
from log_storage.logging_servivce import handle_logger

from apps.questionnaire.services.questionnaire.send_to_bank_service import SendToBankService
from log_storage.logging_config import logger_info


class KafkaConsumerAddSelectedOfferIdService(BaseKafkaConsumerService):
    """
    Консюмер Kafka, который обрабатывает сообщения, добавляя идентификаторы выбранных предложений.
    """

    def __init__(self, topic, group_id='bank-offers-group'):
        kafka_service = KafkaProducerService()
        kafka_config = kafka_service.read_config()
        super().__init__(topic, group_id, kafka_config)

    def process_message(self, msg):
        data = json.loads(msg.value().decode('utf-8'))
        client_id = data.get('client_id')
        offer_ids = data.get('selected_offers')
        offer_ids = convert_str_list(offer_ids)
        SendToBankService.process_offers(client_id, offer_ids)
        handle_logger('BankOfferService worked', logger_info)
