# =========================
# CONEXÂO AO DATABASE
# =========================
# DECORATO
import psycopg2
import os 
from dotenv import load_dotenv

load_dotenv()

def conectar():
    try:

        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            host=os.getenv("DB_HOST"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
            user=os.getenv("DB_USER")
        )
        print("Conectado ao banco de dados")
        return conn 
    except Exception as e:

        print(f"Erro ao se conectar {e}")

