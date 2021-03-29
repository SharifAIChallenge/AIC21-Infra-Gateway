from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from services.kafka_cli import KafkaClient, Topics
import json
import uuid
from apps import permissions


class PlayGameAPIView(GenericAPIView):
    permission_classes = [permissions.IsBackend]

    def post(self, request):
        game_id = uuid.uuid4()

        game_information = dict(request.data)
        game_information['game_id'] = str(game_id)

        KafkaClient.send_message(Topics.PLAY_GAME.value, game_information)
        return Response(data={'game_id': game_id}, status=status.HTTP_200_OK)
