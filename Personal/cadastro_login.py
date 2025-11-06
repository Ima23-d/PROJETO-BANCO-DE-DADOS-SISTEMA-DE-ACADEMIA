# =========================
# CADASTRO E LOGIN DO PERSONAL (Instrutores)
# =========================

import os
import bcrypt
import pwinput
from Query.query import executar_query


# -------------------------
# Funções auxiliares
# -------------------------

def limpar_tela():
    """Limpa o terminal (Windows/Linux)."""
    os.system("cls" if os.name == "nt" else "clear")


def criptografar(password: str) -> str:
    """Criptografa uma senha em texto puro usando bcrypt e retorna como string."""
    senha_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha_bytes, salt)
    return hashed.decode("utf-8")


def checar_password(password: str, hashed: str) -> bool:
    """Verifica se a senha informada corresponde ao hash salvo."""
    senha_bytes = password.encode("utf-8")
    hashed_bytes = hashed.encode("utf-8")
    return bcrypt.checkpw(senha_bytes, hashed_bytes)


# -------------------------
# Funções principais
# -------------------------

def cadastrar_personal():
    limpar_tela()
    print("=== CADASTRO DE PERSONAL ===")

    try:
        nome = input("Nome: ").strip()
        cref = input("CREF: ").strip()
        email = input("Email: ").strip()
        senha = pwinput.pwinput(prompt="Crie sua senha: ", mask="*").strip()

        senha_hash = criptografar(senha)

        query = """
            INSERT INTO Instrutores (Nome, CREF, Email, Senha)
            VALUES (%s, %s, %s, %s)
            RETURNING ID_Instrutor
        """
        res = executar_query(query, (nome, cref, email, senha_hash), fetch=True)

        if res:
            print(f"\nPersonal cadastrado com sucesso! ID: {res[0][0]}")
        else:
            print("\nFalha ao cadastrar personal. Verifique se o email já existe ou se o banco está acessível.")
    except Exception as e:
        print(f"\nErro ao cadastrar personal: {e}")

    input("\nPressione ENTER para continuar...")


def login_personal():
    limpar_tela()
    print("=== LOGIN DO PERSONAL ===")

    try:
        email = input("Email: ").strip()
        senha = pwinput.pwinput(prompt="Senha: ", mask="*").strip()
    except Exception as e:
        print("Digite um valor valido {e}")

    query = "SELECT ID_Instrutor, Nome, Senha FROM Instrutores WHERE Email = %s"
    personal = executar_query(query, (email,), fetch=True)

    if personal:
        id_instrutor, nome_instrutor, senha_hash = personal[0]
        if checar_password(senha, senha_hash):
            print(f"\nBem-vindo(a), {nome_instrutor}!")
            input("Pressione ENTER para continuar...")

            from Personal.menu_personal import menu_personal
            menu_personal(id_instrutor)
        else:
            print("\nSenha incorreta.")
            input("Pressione ENTER para continuar...")
    else:
        print("\nEmail não encontrado. Cadastre-se antes de tentar logar.")
        input("Pressione ENTER para continuar...")
