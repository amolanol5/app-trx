import boto3
from domain.interfaces.auth_get_token_interface import InterfaceAuthToken
from src.commons.config import Config
from src.controllers.out.client_cognito import CognitoClient
from src.utils.hash import hash_secret_cognito

cognito = CognitoClient()


class AuthTokenAdapter(InterfaceAuthToken):
    def get_token(self, username, password):
        response = cognito.client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
                'SECRET_HASH':  hash_secret_cognito(username, Config.COGNITO_CLIENT_ID, Config.COGNITO_CLIENT_SECRET)
            },
            ClientId=Config.COGNITO_CLIENT_ID,

        )
        
        return response
