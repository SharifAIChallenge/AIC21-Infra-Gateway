from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from services.kafka_cli import KafkaClient, Topics
from services.minio_cli import MinioClient
import uuid


class StoreCodeAPIView(GenericAPIView):
    def post(self, request):
        code_id = uuid.uuid4()
        file = request.FILES['file']
        MinioClient.upload(code_id, file)
        KafkaClient.send_message(Topics.STORE_CODE.value, str(code_id))
        return Response(data={'code_id': code_id}, status=status.HTTP_200_OK)



