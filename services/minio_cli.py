from minio import Minio
from django.core.files.base import ContentFile
import enum
import os
from gateway.settings import MINIO_ENDPOINT, MINIO_SECRET_KEY, MINIO_ACCESS_KEY

client = Minio(
    endpoint=MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)


class BucketName(enum.Enum):
    Code = os.getenv('MINIO_BUCKET_CODE')
    Map = os.getenv('MINIO_BUCKET_MAP')
    Log = os.getenv('MINIO_BUCKET_LOG')


for e in BucketName:
    found = client.bucket_exists(e.value)
    if not found:
        client.make_bucket(e.value)


class MinioClient:

    @staticmethod
    def upload(file_id, file, bucket_name, postfix='.zip') -> bool:
        content = ContentFile(file.read())
        try:
            client.put_object(
                bucket_name, f'{file_id}{postfix}', content, length=len(content)
            )
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def get_file(file_id, bucket_name):
        try:
            response = client.get_object(bucket_name, f'{file_id}.zip')
            return response.data
        except Exception as e:
            print(e)
            return None
