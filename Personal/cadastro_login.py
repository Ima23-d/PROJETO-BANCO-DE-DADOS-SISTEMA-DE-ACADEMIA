# =========================
# CADASTRO E LOGIN DO PERSONAL (Instrutores)
# =========================

import os
from Query.query import executar_query
import pwinput

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def cadastrar_personal():
    limpar_tela()
    print("--- CADASTRO DE PERSONAL ---")
    nome = input("Nome: ").strip()
    cref = input("CREF: ").strip()
    email = input("Email: ").strip()
    senha = pwinput.pwinput(prompt="Crie sua senha: ", mask="*").strip()

    query = "INSERT INTO Instrutores (Nome, CREF, Email, Senha) VALUES (%s, %s, %s, %s) RETURNING ID_Instrutor"
    res = executar_query(query, (nome, cref, email, senha), fetch=True)
    if res:
        print(f"\nPersonal cadastrado com sucesso! ID: {res[0][0]}")
    else:
        print("\nFalha ao cadastrar personal. Verifique se o CREF/Email já existem ou se o banco está acessível.")
    input("Pressione ENTER para continuar...")

def login_personal():
    limpar_tela()
    print("--- LOGIN DO PERSONAL ---")
    email = input("Email: ").strip()
    senha = pwinput.pwinput(prompt="Senha: ", mask="*").strip()

    query = "SELECT ID_Instrutor, Nome FROM Instrutores WHERE Email = %s AND Senha = %s"
    personal = executar_query(query, (email, senha), fetch=True)

    if personal:
        from Personal.menu_personal import menu_personal
        print(f"\nBem-vindo(a), {personal[0][1]}!")
        input("Pressione ENTER para continuar...")
        menu_personal(personal[0][0])
    else:
        print("\nEmail ou senha incorretos.")
        input("Pressione ENTER para continuar...")