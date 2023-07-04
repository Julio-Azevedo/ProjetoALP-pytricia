import os
from mainMenu import show_main_menu
from login import login
from register import register
from profileUser import logged

# Chamando o menu principal
opt = show_main_menu()

# Código principal
while opt != "0":
    if opt == "1":
        os.system("clear||cls")
        username = login()
        if username:
            logged(username)
    elif opt == "2":
        os.system("clear||cls")
        register()
    else:
        print("Opção invalida!")
    input("\nPressione Enter para voltar ao menu principal")
    opt = show_main_menu()
os.system("clear||cls")
print("Encerando PyTricia...")