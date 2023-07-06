import os
from menu import menu_usuario
from oraculo import horoscopo, numerologia


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função que é chamada após o login
def perfil(busca):
    option = menu_usuario(busca)
    
    while option != "0":
        if option == "1":
            horoscopo(busca)
        elif option == "2":
            numerologia(busca)
        else:
            print("Opção invalida, Tente novamente!")         
        option = menu_usuario(busca)
    os.system("clear||cls")


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´