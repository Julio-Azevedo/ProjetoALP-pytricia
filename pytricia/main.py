import os
from mainMenu import show_main_menu
from register import register
from about import show_info
from login import login

# chamando o menu
opt = show_main_menu()

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