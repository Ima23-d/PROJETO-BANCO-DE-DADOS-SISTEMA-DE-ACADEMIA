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

#Trocamos o nome da variavel para buscar_aluno e definimos como 'str' ao invés de 'int'
def cadastrar_treino():
    limpar_tela()
    try:
        id_instrutor = int(input("ID do Instrutor: ").strip())
        buscar_aluno = str(input("Nome do Aluno: ").strip())
    except ValueError:
        print("ID's devem ser números inteiros.")
        print("O nome do aluno tem que estar cadastrado.")
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
    #fizemos uma alteração depois de muita pesquisa de como iriamos transferir a busca pelo aluno de ID
    #para nome, e chegamos a conclusão de substituir essa parte inferior que era o código antigo
    #executar_query("SELECT FROM alunos WHERE nome_aluno = %s", (buscar_aluno))
    #executar_query("INSERT INTO treinos_alunos (id_aluno, id_treinos) VALUES (%s, %s)", (id_aluno, treino_id))
    #por um sql_buscar o id do aluno onde o nome do aluno seria como o inserido na variavel buscar_aluno
    #fazendo assim uma pequena burlada pois ele ainda está usando o código de id_do aluno na tabela e 
    #na busca, só que, ao invés do usuário digitar o id do aluno, ele vai digitar o nome, o código irá
    #buscar o nome, e vai pegar o id do aluno que tem esse nome e vai seguir normalmente
    sql_buscar = "SELECT id_aluno FROM alunos WHERE nome_aluno ILIKE %s"
    resultado = executar_query(sql_buscar, (buscar_aluno,), fetch=True)


    if not resultado:
        print("\nAluno não encontrado!")
        input("\nPressione ENTER para voltar...")
        return

    id_aluno = resultado[0][0]  


    sql_insert = "INSERT INTO treinos_alunos (id_aluno, id_treinos) VALUES (%s, %s)"
    executar_query(sql_insert, (id_aluno, treino_id))
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


#Aqui as mudanças foram basicamente as mesmas de lá de cima, somente modificamos o jeito de busca para
#sql_buscar_alunos para SELECT o id do aluno onde o nome do aluno for como o nome digitado pelo personal
#e adicionamos o id_aluno = resultado_aluno[0][0] por que era necessário utilizar uma tupla
#(pelo menos pelo que a gente pesquisou era o unico jeito de se fazer sem precisar alterar nada das tabelas)
def ver_treinos_alunos_personal(nome_aluno=None):
    limpar_tela()

    if nome_aluno is None:
        try:
            nome_aluno = str(input("Digite o nome do aluno para ver os treinos: ").strip())
            sql_buscar_aluno = "SELECT id_aluno FROM alunos WHERE nome_aluno ILIKE %s"
            resultado_aluno = executar_query(sql_buscar_aluno, (f"%{nome_aluno}%",), fetch=True)
        except ValueError:
            print("Nome inválido.")
            input("Pressione ENTER para voltar...")
            return
        

    id_aluno = resultado_aluno[0][0]

    query = """
    SELECT 
        treinos.id_treinos, 
        treinos.especificacoes, 
        instrutores.nome AS nome_instrutor
    FROM treinos
    JOIN instrutores ON treinos.id_instrutor = instrutores.id_instrutor
    JOIN treinos_alunos ON treinos.id_treinos = treinos_alunos.id_treinos
    WHERE treinos_alunos.id_aluno = %s
    """

    resultados = executar_query(query, (id_aluno,), fetch=True)

    print("--- TREINOS CADASTRADOS ---")
    if resultados is None:
        print("Erro ao buscar treinos (verifique o banco).")
    elif not resultados:
        print("Nenhum treino registrado para este aluno.")
    else:
        for treino in resultados:
            id_treino = treino[0]
            especificacoes = treino[1]
            nome_instrutor = treino[2]

            print(f"\n📋 Treino #{id_treino}")
            print(f"🏋️ Instrutor: {nome_instrutor}")
            print(f"📝 Especificações: {especificacoes}")
            print("-" * 40)

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
        #poderia user o match case
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

