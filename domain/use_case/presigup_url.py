from domain.interfaces.presigup_url_interface import PresigupUrl


class PresigUrlUseCase:
    def __init__(self, presig_url: PresigupUrl):
        self.presig_url = presig_url

    def apply(self, bucket_name, object_name):
        print("applying PresigUrlUseCase")
        return self.presig_url.get_presigup_url(bucket_name, object_name)
