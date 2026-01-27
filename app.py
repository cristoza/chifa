import psycopg2
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permite que el HTML hable con el servidor

# --- CONFIGURACIÓN DE TU POSTGRES ---
DB_CONFIG = {
    "host": "localhost",
    "database": "chat",
    "user": "postgres",        # Tu usuario de Postgres
    "password": "retroman80",  # Tu contraseña
    "port": "5432"
}

def procesar_chatbot(mensaje_usuario, ip_usuario):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        # 1. GUARDAR EN EL HISTORIAL (IP, Mensaje, Fecha/Hora)
        # Nota: La fecha_hora se genera sola en Postgres por el DEFAULT CURRENT_TIMESTAMP
        query_historial = """
            INSERT INTO historial_chat (ip_usuario, mensaje_usuario) 
            VALUES (%s, %s)
        """
        cur.execute(query_historial, (ip_usuario, mensaje_usuario))

        # 2. BUSCAR RESPUESTA EN LAS 50 PREGUNTAS
        # Usamos ILIKE para que no importe si escriben en mayúsculas o minúsculas
        query_respuesta = """
            SELECT respuesta FROM consultas 
            WHERE pregunta_clave ILIKE %s 
            LIMIT 1
        """
        cur.execute(query_respuesta, ('%' + mensaje_usuario + '%',))
        resultado = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        if resultado:
            return resultado[0]
        else:
            return "¡Hola! No estoy seguro de eso, pero puedes preguntarme por el Chaufa, el horario o nuestra ubicación. 🥢"

    except Exception as e:
        print(f"Error crítico: {e}")
        return "Lo siento, mi sistema está en mantenimiento. ¡Llámanos por teléfono!"

@app.route('/chat', methods=['POST'])
def chat():
    time.sleep(1.5)
    data = request.json
    user_msg = data.get("message", "")
    
    # Obtener IP (considerando si estás detrás de un proxy/servidor)
    if request.headers.get('X-Forwarded-For'):
        user_ip = request.headers.get('X-Forwarded-For').split(',')[0]
    else:
        user_ip = request.remote_addr

    respuesta_bot = procesar_chatbot(user_msg, user_ip)
    
    return jsonify({"response": respuesta_bot})

if __name__ == '__main__':
    print("🚀 Servidor del Chifa activo en http://127.0.0.1:5000")
    app.run(debug=True, port=5000)