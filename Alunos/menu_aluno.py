# =========================
# MENU ALUNO
# =========================

import os
from Query.query import executar_query
from Alunos.cadastro_login import cadastrar_aluno,login_aluno


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def ver_treinos_aluno(id_aluno):
    limpar_tela()
    print("--- SEUS TREINOS ---")
    query = """
    SELECT t.ID_Treinos, t.Especificacoes, i.Nome
    FROM Treinos t
    JOIN Instrutores i ON t.ID_Instrutor = i.ID_Instrutor
    JOIN Treinos_alunos ta ON t.ID_Treinos = ta.ID_Treinos
    WHERE ta.ID_Aluno = %s
    """
    treinos = executar_query(query, (id_aluno,), fetch=True)
    if treinos is None:
        print("Erro ao buscar treinos (verifique o banco).")
    elif not treinos:
        print("Nenhum treino registrado.")
    else:
        for t in treinos:
            print(f"\nTreino #{t[0]} | Instrutor: {t[2]}\nDescrição: {t[1]}")
    input("\nPressione ENTER para voltar...")

def menu_aluno(id_aluno):
    while True:
        limpar_tela()
        print("--- MENU DO ALUNO ---")
        print("1 - Ver Treinos")
        print("2 - Voltar")
        
        try:
            opcao = int(input("Escolha: "))
        except ValueError as e:
            print(f"\nValor inválido! Digite um número entre 1 e 3. ({e})")
            input("Pressione ENTER para continuar...")
            continue 

        if opcao == "1":
            ver_treinos_aluno(id_aluno)
        elif opcao == "2":
            print("\nVoltando ao menu anterior...")
            input("Pressione ENTER para continuar...")
            break
        else:
            print("Opção inválida.")
            input("Pressione ENTER para continuar...")

def menu_aluno_principal():
    while True:
        limpar_tela()
        print("=== ÁREA DO ALUNO ===")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Voltar")

        try:
            opcao = int(input("Escolha: "))
            return opcao
        except ValueError as e:
            print(f"\nValor inválido! Digite um número entre 1 e 3. ({e})")
            input("Pressione ENTER para continuar...")
            continue 

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            login_aluno()
        elif opcao == "3":
            print("\nVoltando ao menu anterior...")
            input("Pressione ENTER para continuar...")
            break
        else:
            print("Opção inválida.")
            input("Pressione ENTER para continuar...")
