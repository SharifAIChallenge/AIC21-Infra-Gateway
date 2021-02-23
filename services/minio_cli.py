from minio import Minio
from django.core.files.base import ContentFile

client = Minio(
    "185.97.118.190:9000",
    access_key="ngnFxoPBtPZjBS7m4x12Yb1q5FovKGa4Bl9PsENs13nmDTRp",
    secret_key="RuRRYyZKbOwVnkyNRYq1f7CRPq89XqOwFHkxoTY4Epq0fvHh",
    secure=False
)
bucket_name = "code"
found = client.bucket_exists(bucket_name)
if not found:
    client.make_bucket(bucket_name)


class MinioClient:

    @staticmethod
    def upload(file_id, file):
        content = ContentFile(file.read())
        print(len(content))
        client.put_object(
            bucket_name, f'{file_id}.zip', content, length=len(content)
        )
