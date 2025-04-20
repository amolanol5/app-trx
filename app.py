from src.controllers.http.controllers import run_flask

app = run_flask()

if __name__ == "__main__":
    app.run(debug=True)