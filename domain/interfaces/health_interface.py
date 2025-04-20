from abc import abstractmethod
from abc import ABCMeta

class InterfaceHealth(metaclass=ABCMeta):
    @abstractmethod
    def get_health(self):
        pass
