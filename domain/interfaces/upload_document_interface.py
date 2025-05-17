from abc import abstractmethod
from abc import ABCMeta


class Document(metaclass=ABCMeta):
    @abstractmethod
    def upload_document(self, object_name, bucket_name, body):
        pass
