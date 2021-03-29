from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from services.kafka_cli import KafkaClient, Topics
from .serializers import GameRegisterSerializer
import uuid
from apps import permissions


class PlayGameAPIView(GenericAPIView):
    permission_classes = [permissions.IsBackend]
    serializer_class = GameRegisterSerializer

    def post(self, request):
        game_id = uuid.uuid4()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        game_information = serializer.data
        game_information['game_id'] = str(game_id)
        KafkaClient.send_message(Topics.PLAY_GAME.value, game_information)
        return Response(data={'game_id': game_id}, status=status.HTTP_200_OK)
