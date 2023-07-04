import os
from user_menu import user_menu
from profile_functions import ver_perfil

def logado(search, username):
    opt = user_menu(search)
    
    while opt != "0":
        if opt == "1":
            os.system("clear||cls")
            ver_perfil(search)
        elif opt == "2":
            continue
        elif opt == "3":
            os.system("clear||cls")
            print("Oráculos")
        else:
            print("Opção invalida")
        input("\nPressione Enter para voltar ao menu principal")
        opt = user_menu(search)
    os.system("clear||cls")