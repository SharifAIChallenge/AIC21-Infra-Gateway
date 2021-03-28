from minio import Minio
from django.core.files.base import ContentFile
import enum
from gateway.settings import MINIO_ENDPOINT, MINIO_SECRET_KEY, MINIO_ACCESS_KEY

client = Minio(
    endpoint=MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)


class BucketName(enum.Enum):
    Code = 'code'
    Map = 'map'
    Log = 'game-download'


for e in BucketName:
    found = client.bucket_exists(e.value)
    if not found:
        client.make_bucket(e.value)


class MinioClient:

    @staticmethod
    def upload(file_id, file, bucket_name) -> bool:
        content = ContentFile(file.read())
        try:
            client.put_object(
                bucket_name, f'{file_id}.zip', content, length=len(content)
            )
            return True
        except:
            return False

    @staticmethod
    def get_file(file_id, bucket_name):
        try:
            response = client.get_object(bucket_name, f'{file_id}.zip')
            return response.data
        except:
            return None
