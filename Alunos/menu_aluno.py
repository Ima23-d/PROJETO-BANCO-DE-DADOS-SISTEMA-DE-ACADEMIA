# =========================
# MENU DO ALUNO (CRUD)
# =========================

import os
from Query.query import executar_query
from Alunos.cadastro_login import cadastrar_aluno, login_aluno


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def ver_treinos_aluno(id_aluno):
    limpar_tela()
    print("--- SEUS TREINOS ---")

#O erro estava aqui no Query, o erro que dava era que o id_treinos estava ambiguo, ou seja, ele não sabia de onde 
#era o id_treinos pra puxar do banco de dados, então lembrei que em uma das ultimas aulas de banco de dados
#o Franco utilizando o pgadmin especificava onde ficava cada coluna em sua respectiva tabela 
#Exemplo: SELECT treinos.id_treinos, o "treinos." é pra indicar que é da tabela treinos, treinos.especificacoes 
#da tabela treinos e instrutores.nome da tabela de instrutores

    query = """
        SELECT treinos.id_treinos, treinos.especificacoes, instrutores.nome
        FROM treinos
        JOIN instrutores ON treinos.id_instrutor = instrutores.id_instrutor
        JOIN treinos_alunos ON treinos.id_treinos = treinos_alunos.id_treinos
        WHERE treinos_alunos.id_aluno = %s
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


def editar_dados_aluno(id_aluno):
    limpar_tela()
    print("--- EDITAR SEUS DADOS ---")

    nome = input("Novo nome: ").strip()
    peso = input("Novo peso (kg): ").strip()
    gordura = input("Nova gordura corporal (%): ").strip()
    nivel = input("Novo nível (Básico/Intermediário/Avançado): ").strip()
    deficiencia = input("Nova deficiência (ou deixe em branco): ").strip()

    query = """
        UPDATE alunos
        SET nome_aluno = %s, peso = %s, gordura_corporal = %s, nivel = %s, deficiencia = %s
        WHERE id_aluno = %s
    """

    executar_query(query, (nome, peso, gordura, nivel, deficiencia, id_aluno))
    print("\nDados atualizados com sucesso!")
    input("\nPressione ENTER para voltar...")



def deletar_conta_aluno(id_aluno):
    limpar_tela()
    print("--- DELETAR CONTA ---")
    confirm = input("Tem certeza que deseja excluir sua conta? (s/n): ").lower()
    if confirm == "s":
        executar_query("DELETE FROM alunos WHERE id_aluno = %s", (id_aluno,))
        print("Conta excluída com sucesso!")
        input("\nPressione ENTER para sair...")
        return True
    else:
        print("Operação cancelada.")
        input("\nPressione ENTER para voltar...")
        return False



def menu_aluno(id_aluno):
    while True:
        limpar_tela()
        print("=== MENU DO ALUNO ===")
        print("1 - Ver Treinos")
        print("2 - Editar Dados")
        print("3 - Excluir Conta")
        print("4 - Voltar")

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("\nValor inválido! Digite um número de 1 a 4.")
            input("Pressione ENTER para continuar...")
            continue

        if opcao == 1:
            ver_treinos_aluno(id_aluno)
        elif opcao == 2:
            editar_dados_aluno(id_aluno)
        elif opcao == 3:
            if deletar_conta_aluno(id_aluno):
                break
        elif opcao == 4:
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
        except ValueError:
            print("\nValor inválido! Digite 1, 2 ou 3.")
            input("Pressione ENTER para continuar...")
            continue

        if opcao == 1:
            cadastrar_aluno()
        elif opcao == 2:
            login_aluno()
        elif opcao == 3:
            print("\nVoltando ao menu anterior...")
            input("Pressione ENTER para continuar...")
            break
        else:
            print("Opção inválida.")
            input("Pressione ENTER para continuar...")

