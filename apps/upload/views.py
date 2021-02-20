from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .statistic.kafka import Kafka, Topics
from .models import Code
from .serializers import CodeSerializer
import uuid


class StoreCodeAPIView(GenericAPIView):
    def post(self, request):
        code_id = uuid.uuid4()
        file = request.FILES['file']
        self.save_file_minio(file)
        self.send_to_kafka(code_id)
        return Response(data={'code_id': code_id}, status=status.HTTP_200_OK)

    def save_file_minio(self, file):
        pass

    def send_to_kafka(self, code_id):
        message = Code(code_id=code_id)
        Kafka(Topics.STORE_CODE).send_message(message, CodeSerializer)
