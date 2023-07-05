import os
from menu import menu_usuario
from oraculo import horoscopo


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função que é chamada após o login
def perfil(busca):
    option = menu_usuario(busca)
    
    while option != "0":
        if option == "1":
            horoscopo(busca)
        else:
            print("Opção invalida, Tente novamente!")
    input("Pressione ENTER para voltar")
    option = menu_usuario()
os.system("clear||cls")


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´