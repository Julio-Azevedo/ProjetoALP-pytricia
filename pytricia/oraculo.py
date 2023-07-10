import os
from menu import horoscopo_menu, horocopo_mensagem, numerologia_menu, numerologia_nome_mensagem, menu_config_perfil, previsoes_menu, previsoes_mensagem, exibir_historico_menu
from verifica import verifica_horoscopo, definicao_numerologia, verifica_numerologia, salvar_historico
from config import exibir_perfil, editar_perfil, deletar_perfil


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

# Criando função de configurar perfil
def config_perfil(busca):
    option = menu_config_perfil()
    deletado = False 
    
    while option != "0":
        if option == "1":
            os.system("clear||cls")
            exibir_perfil(busca)
            input("Pressione ENTER para voltar")
        elif option == "2":
            os.system("clear||cls")
            editar_perfil(busca)
        elif option == "3":
            os.system("clear||cls")
            deletado = deletar_perfil(busca)
            break
        else:
            print("Opção invalida, tente novamente!") 
        option = menu_config_perfil()
        
    return deletado


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

def previsoes(busca):
    option = previsoes_menu()
    
    while option != "0":
        if option == "1":
            os.system("clear||cls")
            previsao = verifica_horoscopo()
            previsoes_mensagem(previsao, busca)
            salvar_historico(busca, previsao)
            input("Pressione ENTER para voltar")
        elif option == "2":
            os.system("clear||cls")
            exibir_historico_menu(busca)
            input("\nPressione ENTER para voltar")
        else:
            print("Opção invalida, tente novamente!") 
        option = previsoes_menu()
        
        
# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´