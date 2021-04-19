from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from services.kafka_cli import KafkaClient
from gateway.settings import KAFKA_TOPIC_MATCH_0, KAFKA_TOPIC_MATCH_1

from .serializers import GameRegisterSerializer
import uuid
from apps import permissions


class PlayGameAPIView(GenericAPIView):
    permission_classes = [permissions.IsBackend]
    serializer_class = GameRegisterSerializer

    def post(self, request):
        topic = KAFKA_TOPIC_MATCH_0
        priority = request.GET.get('priority', '-1')
        if priority.isnumeric():
            priority = int(priority)
            if priority == 1:
                topic = KAFKA_TOPIC_MATCH_1
        game_id = uuid.uuid4()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        game_information = serializer.data
        game_information['game_id'] = str(game_id)
        KafkaClient.send_message(topic, game_information)
        return Response(data={'game_id': game_id}, status=status.HTTP_200_OK)
