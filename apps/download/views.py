from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from services.minio_cli import BucketName
from gateway.settings import MINIO_DOWNLOAD_LINK_DOMAIN
from apps import permissions


class GameLogAPIView(GenericAPIView):
    permission_classes = [permissions.IsBackend]

    def get(self, request):
        game_id = request.GET.get('game_id')
        player_id = request.GET.get('player_id')
        bucket_name = BucketName.Log.value
        if player_id:
            download_link = f"https://{MINIO_DOWNLOAD_LINK_DOMAIN}/{bucket_name}/{game_id}/{player_id}.log"
        else:
            download_link = f"https://{MINIO_DOWNLOAD_LINK_DOMAIN}/{bucket_name}/{game_id}/{game_id}.log"

        return Response(data={'log': download_link}, status=status.HTTP_200_OK)


class CodeAPIView(GenericAPIView):
    permission_classes = [permissions.IsBackend]

    def get(self, request):
        code_id = request.GET['code_id']
        bucket_name = BucketName.Code.value
        download_link = f"https://{MINIO_DOWNLOAD_LINK_DOMAIN}/{bucket_name}/{code_id}.zip"
        return Response(data={'code': download_link}, status=status.HTTP_200_OK)
