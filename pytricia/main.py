import os
from menu import menu_principal
from login import login
from register import cadastro
from profileUser import logado

# Chamando o menu principal
opt = menu_principal()

# Código principal
while opt != "0":
    if opt == "1":
        os.system("clear||cls")
        login()
    elif opt == "2":
        os.system("clear||cls")
        cadastro()
    else:
        print("Opção invalida!")
    input("\nPressione Enter para voltar ao menu principal")
    opt = menu_principal()
os.system("clear||cls")
print("Encerando PyTricia...")