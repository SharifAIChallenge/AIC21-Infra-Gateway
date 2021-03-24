# import enum
# from kafka import KafkaConsumer
# from backend_cli import BackendCli
# from gateway.settings import KAFKA_END_POINT
# import json
# import time
#
#
# class Topics(enum.Enum):
#     EVENTS = "events"
#
#
# maximum_try_count = 10
#
# consumer = KafkaConsumer(
#     Topics.EVENTS.value,
#     bootstrap_servers=KAFKA_END_POINT,
#     group_id='gateway-test',
#     enable_auto_commit=False,
# )
#
# for message in consumer:
#     data = json.loads(message.value.decode("utf-8"))
#     result = BackendCli.send_event(data)
#     if result:
#         consumer.commit()
#     else:
#         try_count = 0
#         while not BackendCli.send_event(data) and try_count < maximum_try_count:
#             try_count += 1
#             time.sleep(try_count)
#         consumer.commit()
