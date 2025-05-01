import os
from dotenv import load_dotenv

# load variables
load_dotenv()


class Config:
    COGNITO_CLIENT_ID = os.environ.get('COGNITO_CLIENT_ID')
    COGNITO_CLIENT_SECRET = os.environ.get('COGNITO_CLIENT_SECRET')
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
    AWS_REGION = os.environ.get('AWS_REGION')
