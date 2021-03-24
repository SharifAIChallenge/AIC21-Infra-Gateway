from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from services.minio_cli import MinioClient, BucketName


class GameLogAPIView(GenericAPIView):

    def get(self, request):
        game_id = request.GET['game_id']
        player_id = request.GET['player_id']
        # todo
        return Response(data={'log': 'log'}, status=status.HTTP_200_OK)


class CodeAPIView(GenericAPIView):
    def get(self, request):
        code_id = request.GET['code_id']
        # todo
        return Response(data={'code': 'code'}, status=status.HTTP_200_OK)
