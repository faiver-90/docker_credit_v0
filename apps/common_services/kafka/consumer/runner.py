# # services_kafka/runner.py
# from apps.common_services.kafka.consumer.consumer import KafkaConsumerAddSelectedOfferIdService
#
#
# class KafkaConsumerRunner:
#     """
#      Класс для запуска нескольких Kafka-консюмеров.
#      """
#
#     def __init__(self):
#         self.consumers = [
#             KafkaConsumerAddSelectedOfferIdService(topic='database'),
#         ]
#
#     def run_all(self):
#         for consumer in self.consumers:
#             consumer.start()
#
# # @shared_task
# # def run_kafka_consumer():
# #     """
# #     Celery-задача для запуска всех Kafka-консюмеров.
# #     """
# #
# #     print("Запуск всех Kafka Consumers через Celery")
# #     runner = KafkaConsumerRunner()
# #
# #     try:
# #         runner.run_all()  # Запускаем всех консюмеров
# #         print("Все Kafka Consumers успешно выполнены")
# #     except Exception as e:
# #         print(f"Ошибка при выполнении Kafka Consumers: {str(e)}")
