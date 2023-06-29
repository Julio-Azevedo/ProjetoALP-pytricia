import os

def show_main_menu():
    os.system("clear||cls")
    print("==================")
    print("==== PyTricia ====")
    print("==================")
    print("\n")
    print("[1] - Entrar")
    print("[2] - Cadastrar")
    print("[3] - Sobre a PyTricia")
    print("[0] - Sair")
    print("\n")
    option = input("Digite a opção desejada: ")
    return option