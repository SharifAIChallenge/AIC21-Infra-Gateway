from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import GameLogSerializer, PlayerLogSerializer
from services.minio_cli import MinioClient, BucketName


class GameLogAPIView(GenericAPIView):
    serializer_class = GameLogSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            log = MinioClient.get_file(data['game_id'], BucketName.Code.value)
            if not log:
                return Response(data={'error': 'Log Not Found.'}, status=status.HTTP_404_NOT_FOUND)
            return Response(data={'log': log}, status=status.HTTP_200_OK)
        return Response(data={'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class PlayerLogAPIView(GenericAPIView):
    serializer_class = PlayerLogSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(data={'log': serializer.data}, status=status.HTTP_200_OK)

        return Response(data={'error': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)
