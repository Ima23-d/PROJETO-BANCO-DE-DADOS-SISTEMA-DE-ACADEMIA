# =========================
# MENU DO PERSONAL (CRUD)
# =========================

import os
from Query.query import executar_query
from Personal.cadastro_login import cadastrar_personal, login_personal


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def ver_alunos_personal():
    limpar_tela()
    alunos = executar_query("SELECT id_aluno, nome_aluno, email FROM alunos", fetch=True)
    print("--- ALUNOS CADASTRADOS ---")

    if alunos is None:
        print("Erro ao buscar alunos (verifique o banco).")
    elif not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for a in alunos:
            print(f"ID: {a[0]} | Nome: {a[1]} | Email: {a[2]}")
    input("\nPressione ENTER para voltar...")


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

 
    res1 = executar_query(
        "INSERT INTO treinos (especificacoes, id_instrutor) VALUES (%s, %s) RETURNING id_treinos",
        (especificacoes, id_instrutor),
        fetch=True
    )
    if not res1:
        print("Falha ao inserir treino.")
        input("Pressione ENTER para voltar...")
        return

    treino_id = res1[0][0]
    executar_query("INSERT INTO treinos_alunos (id_aluno, id_treinos) VALUES (%s, %s)", (id_aluno, treino_id))
    print("\nTreino cadastrado com sucesso!")
    input("\nPressione ENTER para voltar...")

def editar_treino():
    limpar_tela()
    try:
        id_treino = int(input("ID do treino que deseja editar: ").strip())
    except ValueError:
        print("ID inválido.")
        input("Pressione ENTER para voltar...")
        return

    nova_desc = input("Nova descrição do treino: ").strip()
    executar_query("UPDATE treinos SET especificacoes = %s WHERE id_treinos = %s", (nova_desc, id_treino))
    print("\nTreino atualizado com sucesso!")
    input("\nPressione ENTER para voltar...")



def deletar_treino():
    limpar_tela()
    try:
        id_treino = int(input("ID do treino que deseja excluir: ").strip())
    except ValueError:
        print("ID inválido.")
        input("Pressione ENTER para voltar...")
        return

    executar_query("DELETE FROM treinos_alunos WHERE id_treinos = %s", (id_treino,))
    executar_query("DELETE FROM treinos WHERE id_treinos = %s", (id_treino,))
    print("\nTreino excluído com sucesso!")
    input("\nPressione ENTER para voltar...")



def ver_treinos_alunos_personal():
    limpar_tela()
    query = """
        SELECT id_treinos, especificacoes, nome
        FROM treinos
        JOIN instrutores ON treinos.id_instrutor = instrutores.id_instrutor
        JOIN treinos_alunos ON treinos.id_treinos = treinos_alunos.id_treinos
        WHERE treinos_alunos.id_aluno = %s
    """
    resultados = executar_query(query, fetch=True)

    print("--- TREINOS CADASTRADOS ---")
    if resultados is None:
        print("Erro ao buscar treinos (verifique o banco).")
    elif not resultados:
        print("Nenhum treino registrado.")
    else:
        for r in resultados:
            print(f"\nTreino #{r[1]} | Aluno: {r[0]} | Instrutor: {r[3]}\nDescrição: {r[2]}")
    input("\nPressione ENTER para voltar...")



def menu_personal(id_personal):
    while True:
        limpar_tela()
        print("=== MENU DO PERSONAL ===")
        print("1 - Ver Alunos")
        print("2 - Cadastrar Treino")
        print("3 - Editar Treino")
        print("4 - Excluir Treino")
        print("5 - Ver Todos os Treinos")
        print("6 - Voltar")

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("\nValor inválido! Digite um número entre 1 e 6.")
            input("Pressione ENTER para continuar...")
            continue

        if opcao == 1:
            ver_alunos_personal()
        elif opcao == 2:
            cadastrar_treino()
        elif opcao == 3:
            editar_treino()
        elif opcao == 4:
            deletar_treino()
        elif opcao == 5:
            ver_treinos_alunos_personal()
        elif opcao == 6:
            print("\nVoltando ao menu anterior...")
            input("Pressione ENTER para continuar...")
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

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("\nValor inválido! Digite 1, 2 ou 3.")
            input("Pressione ENTER para continuar...")
            continue

        if opcao == 1:
            cadastrar_personal()
        elif opcao == 2:
            login_personal()
        elif opcao == 3:
            print("\nVoltando ao menu anterior...")
            input("Pressione ENTER para continuar...")
            break
        else:
            print("Opção inválida.")
            input("Pressione ENTER para continuar...")
