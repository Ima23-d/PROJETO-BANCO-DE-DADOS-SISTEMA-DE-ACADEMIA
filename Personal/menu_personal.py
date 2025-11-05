# =========================
# MENU DO PERSONAL
# =========================

import os
from Query.query import executar_query
from Personal.cadastro_login import cadastrar_personal,login_personal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#===============
# VER ALUNO
#===============
def ver_alunos_personal():
    limpar_tela()
    alunos = executar_query("SELECT ID_Aluno, Nome_Aluno, Email FROM Alunos", fetch=True)
    print("--- ALUNOS CADASTRADOS ---")
    if alunos is None:
        print("Erro ao buscar alunos (verifique o banco).")
    elif not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for a in alunos:
            print(f"ID: {a[0]} | Nome: {a[1]} | Email: {a[2]}")
    input("\nPressione ENTER para voltar...")

#==================
# CADASTRAR TREINO
#==================
def cadastrar_treino():
    limpar_tela()
    try:
        id_instrutor = int(input("ID do Instrutor: ").strip())
        id_aluno = int(input("ID do Aluno: ").strip())
    except ValueError:
        print("IDs devem ser números inteiros.")
        input("Pressione ENTER para voltar...")
        return

    especificacoes = input("Descrição do treino: ").strip()
    res1 = executar_query("INSERT INTO Treinos (Especificacoes, ID_Instrutor) VALUES (%s,%s) RETURNING ID_Treinos", (especificacoes, id_instrutor), fetch=True)
    if not res1:
        print("Falha ao inserir treino.")
        input("Pressione ENTER para voltar...")
        return

    treino_id = res1[0][0]
    res2 = executar_query("INSERT INTO Treinos_alunos (ID_Aluno, ID_Treinos) VALUES (%s,%s)", (id_aluno, treino_id))
    if res2 is None:
      
        print("\nTreino cadastrado com sucesso!")
    else:
        print("\nTreino cadastrado com sucesso!")
    input("\nPressione ENTER para voltar...")

def ver_treinos_alunos_personal():
    limpar_tela()
    query = """
    SELECT a.Nome_Aluno, t.Especificacoes, i.Nome
    FROM Treinos t
    JOIN Instrutores i ON t.ID_Instrutor = i.ID_Instrutor
    JOIN Treinos_alunos ta ON t.ID_Treinos = ta.ID_Treinos
    JOIN Alunos a ON a.ID_Aluno = ta.ID_Aluno
    """
    resultados = executar_query(query, fetch=True)
    if resultados is None:
        print("Erro ao buscar treinos (verifique o banco).")
    elif not resultados:
        print("Nenhum treino registrado.")
    else:
        for r in resultados:
            print(f"\nAluno: {r[0]}\nInstrutor: {r[2]}\nTreino: {r[1]}")
    input("\nPressione ENTER para voltar...")

def menu_personal(id_personal):
    while True:
        limpar_tela()
        print("=== MENU DO PERSONAL ===")
        print("1 - Ver alunos")
        print("2 - Cadastrar treino")
        print("3 - Ver todos os treinos")
        print("4 - Voltar")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            ver_alunos_personal()
        elif opcao == "2":
            cadastrar_treino()
        elif opcao == "3":
            ver_treinos_alunos_personal()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
            input("Pressione ENTER para continuar...")

def menu_personal_principal():
    while True:
        limpar_tela()
        print("=== ÁREA DO PERSONAL ===")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Voltar")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar_personal()
        elif opcao == "2":
            login_personal()
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")
            input("Pressione ENTER para continuar...")