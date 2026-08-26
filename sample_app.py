from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "API Segura y Operativa", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)  # nosec B104
