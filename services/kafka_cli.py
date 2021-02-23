import enum
from json import dumps
from kafka import KafkaProducer

kafka_producer = KafkaProducer(
    bootstrap_servers='185.97.118.190:9092', value_serializer=lambda x: dumps(x).encode('utf-8')
)


class Topics(enum.Enum):
    STORE_CODE = "store-code"
    PLAY_GAME = "play-game"


class KafkaClient:
    @staticmethod
    def send_message(topic, message):
        kafka_producer.send(topic=topic, value=message)
