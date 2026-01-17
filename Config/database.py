import psycopg2
from psycopg2 import Error

class Database:
    def __init__(self):
        #Configuración de PostgreSQL
        self.host = "localhost"
        self.user = "postgres"
        self.password = "tu_contraseña" # Recuerda cambiar esto
        self.database = "chifa_db"
        self.port = "5432"
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establece la conexión a la base de datos PostgreSQL."""
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )
            self.cursor = self.conn.cursor()
            print("Conexión exitosa a la base de datos{self.database}.")     
        except (Exception , Error) as error:
            print(f"Error al conectar a PostgreSQL: {e}")

    def get_connection(self):
        """Retorna el objeto de conexión actual. Si no existe, lo crea."""
        if not self.conn or self.conn.closed:
            self.connect()
        return self.conn
    
    def disconnect(self):
        """Cierra la conexión activa."""
        if self.conn:
            if self.cursor:
                self.cursor.close()
            self.conn.close()
            print("Conexión a la base de datos cerrada.")

#Singleton instance para uso facil en toda la app
db = Database()