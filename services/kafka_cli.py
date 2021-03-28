import enum
from json import dumps
from kafka import KafkaProducer
from gateway.settings import KAFKA_END_POINT

# kafka_producer = KafkaProducer(
#     bootstrap_servers=KAFKA_END_POINT, value_serializer=lambda x: dumps(x).encode('utf-8')
# )
kafka_producer = 0

class Topics(enum.Enum):
    STORE_CODE = "store-code"
    PLAY_GAME = "play-game"


class KafkaClient:
    @staticmethod
    def send_message(topic, message) -> bool:
        try:
            kafka_producer.send(topic=topic, value=message)
            kafka_producer.flush()
            return True
        except Exception as e:
            print(e)
            return False
