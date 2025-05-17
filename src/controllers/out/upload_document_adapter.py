import requests
from domain.interfaces.upload_document_interface import Document
from src.controllers.out.client_s3 import S3Client

s3 = S3Client()


class DocumentAdapter(Document):
    def upload_document(self, bucket_name, object_name, body):
        try:
            # Sube el documento
            print("DocumentAdapter - Subiendo documento")
            response = s3.client.put_object(
                Bucket=bucket_name,
                Key=object_name,
                Body=body
            )
            print("DocumentAdapter", response)
            return response
        except Exception as e:
            print(f"DocumentAdapter - Ocurrió un error: {e}")
            
            
            
