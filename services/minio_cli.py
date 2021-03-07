from minio import Minio
from django.core.files.base import ContentFile
import enum

client = Minio(
    "185.97.118.190:9001",
    access_key="ngnFxoPBtPZjBS7m4x12Yb1q5FovKGa4Bl9PsENs13nmDTRp",
    secret_key="RuRRYyZKbOwVnkyNRYq1f7CRPq89XqOwFHkxoTY4Epq0fvHh",
    secure=False
)


class BucketName(enum.Enum):
    Code = 'code'
    Map = 'map'
    Log = 'log'


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
