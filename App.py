from flask import Flask
from config.database import db
import sys 

app = Flask (__name__)

@app.route("/")
def index():
    return "<h1> Bienvenido al sistema Chifa</h1> <p> La aplicacion está corriendo. </p>"

def main():
    print("Iniciando aplicacion web...")

    # Verificar conexion a BD antes de arrancar la app
    try:
        conn = db.get_connection()
        if conn:
            print("Conexion a PostgreSQL: Ok.")
            db.disconnect()
    except Exception as e:
        print(f"Advertencia: no se pudo conectar a la base de datos: {e}")


    app.run(debug=True, port=5000)



if __name__ == "__main__":
    main()