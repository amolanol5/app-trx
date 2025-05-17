from domain.interfaces.presigup_url_interface import PresigupUrl
from src.controllers.out.client_s3 import S3Client

s3 = S3Client()


class PresigUrlAdapter(PresigupUrl):
    def get_presigup_url(self, bucket_name, object_name):
        response = s3.client.generate_presigned_post(
            bucket_name,
            object_name,
        )

        return response
