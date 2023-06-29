import os
from logMenu import show_log_menu

def logged(search):
    opt = show_log_menu(search)
    
    while opt != "0":
        if opt == "1":
            os.system("clear||cls")
            print(f"Perfil de {search['username']}")
            print(f"Nome de usuário: {search['username']}")
            print(f"Senha de usuário: {search['password']}")
            print(f"Senha de usuário: {search['birth']}")
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