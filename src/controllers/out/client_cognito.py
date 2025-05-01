import boto3
from src.commons.config import Config

class CognitoClient:
    def __init__(self, aws_access_key=None, aws_secret_key=None, region=None):
        self.client = boto3.client(
            'cognito-idp',
            aws_access_key_id=aws_access_key or Config.AWS_ACCESS_KEY,
            aws_secret_access_key=aws_secret_key or Config.AWS_SECRET_KEY,
            region_name=region or Config.AWS_REGION
        )