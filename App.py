from flask  import Flask 
from Config.database import db
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return " <h1> Bienvenido al Sistema Chifa </h1><p> La aplicaccion esta corriendo correctamente. </p> "

def main():
    print("Iniciando la aplicacion web...")

    #Verificar a B antes de arrancar
    try:

        conn = db.get_connection()
        if conn:
            print("Conexion a PostgresSQL: OK.")
            db.disconnect()
    except Exception as e:
        print(f"Advertencia: No se pudo conectar a la base de datos. {e}")

    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()

