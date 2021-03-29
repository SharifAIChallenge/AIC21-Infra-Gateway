from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from services.kafka_cli import KafkaClient, Topics
from services.minio_cli import MinioClient, BucketName
import uuid
from apps import permissions


class StoreCodeAPIView(GenericAPIView):
    permission_classes = [permissions.IsBackend]

    def post(self, request):
        language = request.data['language']
        code_id = uuid.uuid4()
        file = request.FILES['file']

        successful_upload_to_minio = MinioClient.upload(code_id, file, BucketName.Code.value)
        if not successful_upload_to_minio:
            return Response(data={'error': 'minio server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        kafka_message = {'code_id': str(code_id), 'language': language}
        successful_send_to_kafka = KafkaClient.send_message(Topics.STORE_CODE.value, kafka_message)
        if not successful_send_to_kafka:
            return Response(data={'error': 'kafka server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data={'code_id': code_id}, status=status.HTTP_200_OK)


class StoreMapAPIView(GenericAPIView):
    permission_classes = [permissions.IsBackend]

    def post(self, request):
        map_id = uuid.uuid4()
        file = request.FILES['file']

        successful_upload_to_minio = MinioClient.upload(map_id, file, BucketName.Map.value, postfix='')
        if not successful_upload_to_minio:
            return Response(data={'error': 'minio server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(data={'map_id': map_id}, status=status.HTTP_200_OK)
