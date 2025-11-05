# =========================
# FUNÇÃO EXECUTAR QUERY
# =========================

from config.config import conectar

def executar_query(query, params=None, fetch=False):
    conn = conectar()
    if not conn:
        print("Erro: conexão não estabelecida.")
        return None

    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        resultado = cursor.fetchall() if fetch else None
        conn.commit()
        cursor.close()
        conn.close()
        return resultado
    except Exception as e:
        print(f"Erro ao executar query: {e}")
        try:
            conn.rollback()
            cursor.close()
            conn.close()
        except:
            pass
        return None