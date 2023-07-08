import os
from menu import horoscopo_menu, horocopo_mensagem, numerologia_menu, numerologia_nome_mensagem
from verifica import verifica_horoscopo, definicao_numerologia, verifica_numerologia


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função do horoscopo
def horoscopo(busca):
    option = horoscopo_menu()
    
    while option != "0":
        if option == "1":
            os.system("clear||cls")
            astral = verifica_horoscopo()
            horocopo_mensagem(astral, busca)
            input("Pressione ENTER para voltar")
        else:
            print("Opção invalida, tente novamente!") 
        option = horoscopo_menu()      


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função da numerologia
def numerologia(busca):
    option = numerologia_menu()
    
    while option != "0":
        if option == "1":
            os.system("clear||cls")
            nome = busca['username'].upper()
            numero = verifica_numerologia(nome)
            carta, definicao = definicao_numerologia(numero)
            numerologia_nome_mensagem(nome, carta, definicao)
            input("Pressione ENTER para voltar")
        else:
            print("Opção invalida, tente novamente!")
        option = numerologia_menu()


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´