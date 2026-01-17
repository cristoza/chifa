import psycopg2
from psycopg2 import Error

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "postgres"
        self.password = "PC4admin"
        self.database = "CHIFA"
        self.port = "5432"

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.conn.cursor()
            print("Conexion exitosa a la base de datos.")
        except Error as error:
            print(f"Error al conectar a PostgreSQL: {error}")

    def get_connection(self):
        if not self.conn or self.conn.closed:
            self.connect()
        return self.conn
    def disconnect(self):
        if self.conn:
            if self.cursor:
                self.cursor.close()
            self.conn.close()
            print("Conexion a PostgreSQL cerrada.")

# Singleton instance
db=Database() 