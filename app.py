from src.controllers.http.controllers import run_flask
from src.commons.config import Config

app = run_flask()

if __name__ == "__main__":
    app.run(debug=True, port=Config.APP_PORT, host=Config.HOST)