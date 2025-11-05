# =========================
# FUNÇÃO EXECUTAR QUERY (CORRIGIDA)
# =========================

from config.config import conectar

def executar_query(query, params=None, fetch=False):
 
    conn = conectar()
    if not conn:
        print("Erro: conexão não estabelecida.")
        return None

    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)

        resultado = None
        if fetch:
            resultado = cursor.fetchall()

        conn.commit()
        return resultado

    except Exception as e:
        print(f"Erro ao executar query: {e}")
        conn.rollback()
        return None

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
