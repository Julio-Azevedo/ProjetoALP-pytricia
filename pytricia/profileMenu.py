import os
# Função do menu do usuário logado 
def show_log_menu(search):
    os.system("clear||cls")
    print(f"Bem vindo a PyTricia {search['username']}")
    while True:
        print("\n")
        print("[1] - Ver perfil")
        print("[2] - Editar perfil")
        print("[3] - Previsão do dia")
        print("\n")
        option = input("Digite a opção desejada: ")
        return option