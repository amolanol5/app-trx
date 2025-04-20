from domain.interfaces.health_interface import InterfaceHealth

class HealthUseCase:
    def __init__(self, health : InterfaceHealth):
        self.health = health
        
    def apply(self):
        return self.health.get_health()