import os
from menu import menu
from login import login
from cadastro import cadastro


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Chama a função menu para exibir o menu e obter a opção selecionada
option = menu()


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

while option != "0":
    if option == "1":
        login()
    elif option == "2":
        cadastro()
    else:
        print("Opção invalida, Tente novamente!")
    input("Pressione ENTER para voltar")
    option = menu()
os.system("clear||cls")


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´