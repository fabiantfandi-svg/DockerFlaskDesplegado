from flask import Flask

app = Flask(__name__)

MYSQL_PASSWORD = "super_secret_123"

@app.route("/")
def index():
    return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
