import os
from menu import menu_usuario
from oraculo import horoscopo, numerologia, config_perfil, previsoes


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função que é chamada após o login
def perfil(busca):
    option = menu_usuario(busca)
    
    while option != "0":
        if option == "1":
            previsoes(busca)
        elif option == "2":
            horoscopo(busca)
        elif option == "3":
            numerologia(busca)
        elif option == "4":
            deletado = config_perfil(busca)
            if deletado:
                return
        else:
            print("Opção invalida, Tente novamente!")         
        option = menu_usuario(busca)
    os.system("clear||cls")


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´