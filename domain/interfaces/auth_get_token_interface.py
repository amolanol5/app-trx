from abc import abstractmethod
from abc import ABCMeta

class InterfaceAuthToken(metaclass=ABCMeta):
    @abstractmethod
    def get_token(self, username, password):
        pass
