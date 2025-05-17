from abc import abstractmethod
from abc import ABCMeta

class PresigupUrl(metaclass=ABCMeta):
    @abstractmethod
    def get_presigup_url(self):
        pass