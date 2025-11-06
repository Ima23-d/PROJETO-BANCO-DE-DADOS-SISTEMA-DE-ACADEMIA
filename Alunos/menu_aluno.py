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
    SELECT 
    treinos.id_treinos,
    treinos.especificacoes,
    instrutores.nome AS nome_instrutor
FROM treinos
JOIN instrutores 
    ON treinos.id_instrutor = instrutores.id_instrutor
JOIN treinos_alunos 
    ON treinos.id_treinos = treinos_alunos.id_treinos
WHERE treinos_alunos.id_aluno = %s;

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
        except ValueError as e:
            print(f"\nValor inválido! Digite um número entre 1 e 3. ({e})")
            input("Pressione ENTER para continuar...")
            continue  

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            login_aluno()
        elif opcao == 3:
            print("\nVoltando ao menu anterior...")
            input("Pressione ENTER para continuar...")
            break  # sai do loop e volta ao menu principal
        else:
            print("Opção inválida.")

            input("Pressione ENTER para continuar...")
