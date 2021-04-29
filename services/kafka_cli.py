import enum
import os
from json import dumps
from kafka import KafkaProducer
from gateway.settings import KAFKA_ENDPOINT

kafka_producer = KafkaProducer(
    bootstrap_servers=KAFKA_ENDPOINT, value_serializer=lambda x: dumps(x).encode('utf-8')
)


class Topic:
    def __init__(self, topic_name, total_partitions):
        self.total_partitions = total_partitions
        self.cur = 0
        self.topic_name = topic_name

    def get_partition(self):
        self.cur = (self.cur + 1) % self.total_partitions
        return self.cur


arenas = [Topic(os.getenv("KAFKA_TOPIC_MATCH_0"), os.getenv("KAFKA_TOPIC_MATCH_0_NUM_PARTITIONS")),
          Topic(os.getenv("KAFKA_TOPIC_MATCH_1"), os.getenv("KAFKA_TOPIC_MATCH_1_NUM_PARTITIONS")),
          ]


class Topics(enum.Enum):
    STORE_CODE = os.getenv('KAFKA_TOPIC_STORE_CODE')
    PLAY_GAME = os.getenv('KAFKA_TOPIC_MATCH')


class KafkaClient:
    @staticmethod
    def send_message(priority, message) -> bool:
        try:
            arena = arenas[priority]
            kafka_producer.send(topic=arena.topic_name, value=message, partition=arena.get_partition())
            kafka_producer.flush()
            return True
        except Exception as e:
            print(e)
            return False
