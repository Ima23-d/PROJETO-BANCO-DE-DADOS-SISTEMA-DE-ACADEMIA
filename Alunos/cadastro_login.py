# =========================
# CADASTRO E LOGIN DO ALUNO
# =========================

import os
from Query.query import executar_query

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
    
def cadastrar_aluno():
    limpar_tela()
    print("--- CADASTRO DE ALUNO ---")
    try:
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        data_nasc = input("Data de Nascimento (YYYY-MM-DD): ").strip()
        idade = int(input("Idade: ").strip())
        peso = float(input("Peso (kg): ").strip())
        gordura = float(input("Gordura corporal (%): ").strip())
        nivel = input("Nível (iniciante/intermediário/avançado): ").strip()
        deficiencia = input("Deficiência (se houver): ").strip()
        email = input("Email: ").strip()
        sexo = input("Sexo (M/F): ").strip()
    except Exception as e:
        print(f"Entrada inválida: {e}")
        input("Pressione ENTER para voltar...")
        return

    query = """
    INSERT INTO Alunos
      (Nome_Aluno, CPF, Data_Nascimento, Idade, Peso, Gordura_Corporal, Nivel, Deficiencia, Email, Sexo)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    RETURNING ID_Aluno
    """
    res = executar_query(query, (nome, cpf, data_nasc, idade, peso, gordura, nivel, deficiencia, email, sexo), fetch=True)
    if res:
        print(f"\nAluno cadastrado com sucesso! ID: {res[0][0]}")
    else:
        print("\nFalha ao cadastrar aluno. Verifique se o email/CPF já existem ou se o banco está acessível.")
    input("Pressione ENTER para continuar...")

def login_aluno():
    limpar_tela()
    print("--- LOGIN DE ALUNO ---")
    email = input("Email: ").strip()
    cpf = input("CPF: ").strip()

    query = "SELECT ID_Aluno, Nome_Aluno FROM Alunos WHERE Email = %s AND CPF = %s"
    aluno = executar_query(query, (email, cpf), fetch=True)

    if aluno:
        from Alunos.menu_aluno import menu_aluno
        print(f"\nBem-vindo(a), {aluno[0][1]}!")
        input("Pressione ENTER para continuar...")
        menu_aluno(aluno[0][0])
    else:
        print("\nEmail ou CPF incorretos ou aluno não cadastrado.")
        input("Pressione ENTER para continuar...")