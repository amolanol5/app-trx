
import datetime
from domain.interfaces.health_interface import InterfaceHealth


class HealthAdapter(InterfaceHealth):
    def get_health(self):
        return {
            "message": "I'm alive",
            "time": datetime.datetime.now()
        }
