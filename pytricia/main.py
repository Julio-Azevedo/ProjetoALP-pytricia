import os
from mainMenu import show_main_menu
from login import login
from register import register
from about import show_info

# Chamando o menu principal
opt = show_main_menu()

# Código principal
while opt != "0":
    if opt == "1":
        os.system("clear||cls")
        login()
    elif opt == "2":
        os.system("clear||cls")
        register()
    elif opt == "3":
        os.system("clear||cls")
        show_info()
    else:
        print("Opção invalida!")
    input("\nPressione Enter para voltar ao menu principal")
    opt = show_main_menu()
os.system("clear||cls")
print("Encerando PyTricia...")