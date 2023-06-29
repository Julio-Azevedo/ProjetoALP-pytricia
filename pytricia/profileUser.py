import os
from profileMenu import show_log_menu
from profileEdit import edit_profile
from mainMenu import show_main_menu

def logged(search, username):
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
            edit_profile(search, username, edited=False)
            show_main_menu()
        elif opt == "3":
            os.system("clear||cls")
            print("Previsão")
            break
        else:
            print("Opção invalida")
        input("\nPressione Enter para voltar ao menu principal")
        opt = show_log_menu(search)
    os.system("clear||cls")