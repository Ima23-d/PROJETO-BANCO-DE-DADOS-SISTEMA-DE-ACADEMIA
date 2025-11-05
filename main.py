# =========================
# MENU PRINCIPAL
# =========================

from Alunos.menu_aluno import menu_aluno_principal
from Personal.menu_personal import menu_personal_principal
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def menu_principal():
    while True:
        limpar_tela()
        print("=== SISTEMA DE ACADEMIA ===")
        print("1 - Aluno")
        print("2 - Personal")
        print("3 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            menu_aluno_principal()
        elif opcao == "2":
            menu_personal_principal()
        elif opcao == "3":
            print("\nSaindo do sistema...")
            break
        else:
            print("Opção inválida.")
            input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    menu_principal()
