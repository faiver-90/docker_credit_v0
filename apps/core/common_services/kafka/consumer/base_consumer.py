# import signal
# import sys
#
# from confluent_kafka import Consumer, KafkaException
#
# from apps.core.common_services.kafka.kafka_service import KafkaProducerService
#
#
# class BaseKafkaConsumerService:
#     """
#     Базовый класс для Kafka-консюмеров, который отвечает за настройку и управление потреблением сообщений из Kafka-темы.
#     """
#
#     def __init__(self, topic, group_id='default-group', kafka_config=None):
#         self.topic = topic
#         self.group_id = group_id
#         if kafka_config is None:
#             kafka_config = self.get_kafka_config()
#         self.kafka_config = kafka_config
#         self.consumer = None
#         self.configure_consumer()
#         self.running = True
#
#     def get_kafka_config(self):
#         kafka_service = KafkaProducerService()
#         return kafka_service.read_config()
#
#     def configure_consumer(self):
#         config = self.kafka_config
#         config['group.id'] = self.group_id
#         config['auto.offset.reset'] = 'earliest'
#         self.consumer = Consumer(config)
#         self.consumer.subscribe([self.topic])
#
#     def process_message(self, msg):
#         """Этот метод должен быть переопределен в наследуемом классе."""
#         raise NotImplementedError("Метод process_message должен быть переопределен в наследуемом классе")
#
#     def start(self):
#         print(f'Starting Kafka consumer for topic: {self.topic}')
#
#         signal.signal(signal.SIGTERM, self.stop)
#         signal.signal(signal.SIGINT, self.stop)
#
#         try:
#             while self.running:
#                 msg = self.consumer.poll(0.1)
#                 if msg is None:
#                     continue
#                 if msg.error():
#                     raise KafkaException(msg.error())
#
#                 if not msg.value():
#                     print('Received an empty or None message')
#                     continue
#
#                 self.process_message(msg)
#
#         except KeyboardInterrupt:
#             print("Consumer interrupted by user")
#         finally:
#             self.stop()
#
#     def stop(self, *args):
#         print("Stopping Kafka consumer")
#         self.running = False
#         if self.consumer:
#             self.consumer.close()
#         sys.exit(0)
