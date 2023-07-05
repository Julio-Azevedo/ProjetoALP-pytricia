import os
import datetime
from menu import horoscopo_menu, horocopo_mensagem
from verifica import verifica_horoscopo


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função do horoscopo
def horoscopo(busca):
    option = horoscopo_menu()
    
    while option != "0":
        if option == "1":
            os.system("clear||cls")
            astral = verifica_horoscopo()
            horocopo_mensagem(astral, busca)
        elif option == "2":
            pass
        elif option == "3":
            pass
        else:
            print("Opção invalida, tente novamente!") 
        input("Pressione ENTER para voltar")
        option = horoscopo_menu()      


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´