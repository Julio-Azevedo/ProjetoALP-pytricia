import os
from user_roles.logMenu import show_log_menu

def logged(search):
    opt = show_log_menu(search)
    
    while opt != "0":
        if opt == "1":
            os.system("clear||cls")
            print(f"Perfil do usuário")
            print(f"Nome do usuário: {search['username']}")
            print(f"Senha do usuário: {search['password']}")
            print(f"Data de nascimento do usuário: {search['birth']}")
        elif opt == "2":
            os.system("clear||cls")
            print("A fazer")
        elif opt == "3":
            os.system("clear||cls")
            print("Deslogando...")
            break
        else:
            print("Opção invalida")
        input("\nPressione Enter para voltar ao menu principal")
        opt = show_log_menu(search)
    os.system("clear||cls")