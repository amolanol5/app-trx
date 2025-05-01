from domain.interfaces.auth_get_token_interface import InterfaceAuthToken


class AuthToken:
    def __init__(self, auth_token: InterfaceAuthToken):
        self.auth_token = auth_token

    def apply(self, username, password):
        return self.auth_token.get_token(username, password)
