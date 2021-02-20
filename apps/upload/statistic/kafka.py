from logpipe import Producer
import enum


class Topics(enum.Enum):
    STORE_CODE = "store-code"
    PLAY_GAME = "play-game"


class Kafka:

    def __init__(self, topic_name):
        self.topic_name = topic_name

    def send_message(self, message, serializer_class):
        producer = Producer(self.topic_name, serializer_class)
        producer.send(message)
