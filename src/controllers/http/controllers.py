from flask import Flask, request
from domain.use_case.get_health import HealthUseCase
from src.controllers.http.health_adapter import HealthAdapter
from src.controllers.out.auth_get_token_adapter import AuthTokenAdapter
from domain.use_case.auth_get_token import AuthToken

def run_flask():
    
    app = Flask(__name__)
    
    # health
    health_adapter = HealthAdapter() 
    service_health = HealthUseCase(health_adapter)
    
    # authToken
    auth_token_adapter = AuthTokenAdapter()
    service_auth_token = AuthToken(auth_token_adapter)
    

    @app.route("/health")
    def execute():
        return service_health.apply()
    
    @app.route('/token', methods=['POST'])
    def executes():
        if request.method == 'POST':
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
        
        return service_auth_token.apply(username, password)
    
    return app