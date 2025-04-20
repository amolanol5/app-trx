from flask import Flask
from domain.use_case.get_health import HealthUseCase
from src.controllers.http.health_adapter import HealthAdapter 

def run_flask():
    
    app = Flask(__name__)
    health_adapter = HealthAdapter() 
    service_health = HealthUseCase(health_adapter)

    @app.route("/health")
    def execute():
        return service_health.apply()
    
    return app