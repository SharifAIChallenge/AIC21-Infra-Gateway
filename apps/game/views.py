from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from services.kafka_cli import KafkaClient, Topics
from gateway.settings import KAFKA_TOPIC_MATCH_0, KAFKA_TOPIC_MATCH_1

import json
import uuid


class PlayGameAPIView(GenericAPIView):
    def post(self, request):
        topic = KAFKA_TOPIC_MATCH_0
        priority = request.GET.get('priority', '-1')
        if priority.isnumeric():
            priority = int(priority)
            if priority == 1:
                topic = KAFKA_TOPIC_MATCH_1
        game_id = uuid.uuid4()
        game_information = json.loads(request.body)
        game_information['game_id'] = str(game_id)
        KafkaClient.send_message(topic, game_information)
        return Response(data={'game_id': game_id}, status=status.HTTP_200_OK)
