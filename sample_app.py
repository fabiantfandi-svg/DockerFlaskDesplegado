import os
from flask import Flask
import pymysql

sample = Flask(__name__)

@sample.route("/")
def home():
    try:
        conn = pymysql.connect(
            host=os.getenv('SERVER_HOST', 'servidor-bd-ejemplo'),
            user=os.getenv('SERVER_USER', 'root'),
            password=os.getenv('SERVER_SSH_KEY'),
            database=os.getenv('MYSQL_DATABASE', 'cba_backend_db')
        )
        conn.close()
        db_status = "Conexión exitosa a la base de datos"
    except Exception as e:
        db_status = f"Error al conectar a la base de datos: {e}"

    return f"<h1>Bienvenido a mi aplicación Flask</h1><p>{db_status}</p>"

if __name__ == "__main__":
    host_ip = os.getenv("FLASK_RUN_HOST", "127.0.0.1")
    modo_debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    
    sample.run(host=host_ip, port=5050, debug=modo_debug)  
