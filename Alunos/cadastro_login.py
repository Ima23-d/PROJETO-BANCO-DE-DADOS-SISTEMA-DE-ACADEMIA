# =========================
# CADASTRO E LOGIN DO ALUNO
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


def criptografar(password: str) -> bytes:
    """Criptografa uma senha em texto puro usando bcrypt."""
    senha_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha_bytes, salt)
    return hashed


def checar_password(password: str, hashed: bytes) -> bool:
    """Verifica se a senha informada corresponde ao hash salvo."""
    senha_bytes = password.encode("utf-8")
    return bcrypt.checkpw(senha_bytes, hashed)


# -------------------------
# Funções principais
# -------------------------

def cadastrar_aluno():
    limpar_tela()
    print("=== CADASTRO DE ALUNO ===")

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
        sexo = input("Sexo (M/F): ").upper().strip()
        senha = pwinput.pwinput(prompt="Digite a sua senha: ", mask="*")
        senha_hash = criptografar(senha)

    except Exception as e:
        print(f"\nEntrada inválida: {e}")
        input("Pressione ENTER para voltar...")
        return

    query = """
        INSERT INTO Alunos
        (Nome_Aluno, CPF, Data_Nascimento, Idade, Peso, Gordura_Corporal,
         Nivel, Deficiencia, Email, Sexo, Senha)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING ID_Aluno
    """

    res = executar_query(
        query, (nome, cpf, data_nasc, idade, peso, gordura,
                nivel, deficiencia, email, sexo, senha_hash), fetch=True
    )

    if res:
        print(f"\nAluno cadastrado com sucesso! ID: {res[0][0]}")
    else:
        print("\nFalha ao cadastrar aluno. Verifique se o email/CPF já existem ou se o banco está acessível.")
    input("\nPressione ENTER para continuar...")


def login_aluno():
    limpar_tela()
    print("=== LOGIN DE ALUNO ===")

    try:
        email = input("Email: ").strip()
        senha = pwinput.pwinput(prompt="Senha: ", mask="*").strip()
    except Exception as e:
        print("Digite um valor valido {e}")

    query = "SELECT ID_Aluno, Nome_Aluno, Senha FROM Alunos WHERE Email = %s"
    aluno = executar_query(query, (email,), fetch=True)

    if aluno:
        id_aluno, nome_aluno, senha_hash = aluno[0]
        if checar_password(senha, senha_hash.encode('utf-8')):
            print(f"\nBem-vindo(a), {nome_aluno}!")
            input("Pressione ENTER para continuar...")

            from Alunos.menu_aluno import menu_aluno
            menu_aluno(id_aluno)
        else:
            print("\nSenha incorreta.")
            input("Pressione ENTER para continuar...")
    else:
        print("\nEmail não encontrado. Cadastre-se antes de tentar logar.")
        input("Pressione ENTER para continuar...")
