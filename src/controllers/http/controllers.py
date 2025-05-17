from flask import Flask, request
from domain.use_case.get_health import HealthUseCase
from src.controllers.http.health_adapter import HealthAdapter
from src.controllers.out.auth_get_token_adapter import AuthTokenAdapter
from domain.use_case.auth_get_token import AuthToken
from domain.use_case.presigup_url import PresigUrlUseCase
from src.controllers.out.presig_url_adapter import PresigUrlAdapter
from src.dependencies import service_document


def run_flask():
    
    app = Flask(__name__)
    
    # health
    health_adapter = HealthAdapter() 
    service_health = HealthUseCase(health_adapter)
    
    # authToken
    auth_token_adapter = AuthTokenAdapter()
    service_auth_token = AuthToken(auth_token_adapter)
    
    #presig_url
    presig_url_adapter = PresigUrlAdapter()
    service_presig_url = PresigUrlUseCase(presig_url_adapter)
    
    
    
    
    @app.route("/health")
    def execute():
        return service_health.apply()
    
    @app.route('/token', methods=['POST'])
    def get_token():
        if request.method == 'POST':
            data = request.get_json()
            username = data.get('username')
            password = data.get('password')
        
        return service_auth_token.apply(username, password)
    
    @app.route('/presig_url', methods=['POST'])
    def get_presig_url():
        if request.method == 'POST':
            data = request.get_json()
            bucket_name = data.get('bucket_name')
            object_name = data.get('object_name')
        
        return service_presig_url.apply(bucket_name,object_name)    
    
    @app.route('/upload_document', methods=['POST'])
    def upload_document():
        if request.method == 'POST':
            data = request.get_json()
            bucket_name = data.get('bucket_name')
            object_name = data.get('object_name')
            body = data.get('body')
            
        return service_document.apply(bucket_name,object_name,body)  

    return app