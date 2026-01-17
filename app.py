from flask import Flask
from config.database import db
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Bienvenido al Sistema Chifa</h1><p>La aplicación está corriendo.</p>"

def main():
    print("Iniciando aplicación web...")
    
    # Verificar conexión a BD antes de arrancar
    try:
        conn = db.get_connection()
        if conn:
            print("Conexión a PostgreSQL: OK")
            db.disconnect()
    except Exception as e:
        print(f"Advertencia: No se pudo conectar a la base de datos: {e}")

    # Iniciar servidor web
    # Esto mostrará en consola: Running on http://127.0.0.1:5000
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
