import json

from confluent_kafka import Producer


class KafkaProducerService:
    """
      Класс для работы с Kafka-продюсером, включает методы для чтения конфигурации и отправки данных в Kafka-тему.
    """

    @staticmethod
    def read_config():
        """Чтение конфигурации из файла client.properties"""

        config = {}
        with open("credit_v0/services/kafka/client.properties") as fh:
            for line in fh:
                line = line.strip()
                if len(line) != 0 and line[0] != "#":
                    parameter, value = line.strip().split('=', 1)
                    config[parameter] = value.strip()
        return config

    def send_to_kafka(self, data, topic, key):
        config = self.read_config()
        producer = Producer(config)
        producer.produce(topic, key=str(key), value=json.dumps(data))
        producer.flush()
