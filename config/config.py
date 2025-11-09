# =========================
# CONEXÂO AO DATABASE
# =========================

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
        print("Conectado ao banco de dados!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None

def criar_tabelas():
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        try:
            with open("criar_tabelas.sql", "r", encoding="utf-8") as file:
                sql_script = file.read()
            cursor.execute(sql_script)
            conn.commit()
            print("Script SQL executado com sucesso na nuvem!")
        except FileNotFoundError as e:
            print(f"Erro: Arquivo SQL não encontrado. ({e})")
        except Exception as e:
            print(f"Erro ao executar script SQL: {e}")
        finally:
            cursor.close()
            conn.close()
