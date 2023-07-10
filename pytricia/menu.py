import os
import json
import datetime
import textwrap
from verifica import verifica_numerologia

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função do menu iniciar
def menu():
    os.system("clear||cls")
    conteudo = 40
    menu_opcoes = {
        "1": "Login",
        "2": "Cadastro",
        "0": "Sair"
    }
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Bem-vindo a PyTricia': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Menu': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
        
    option = input("Digite a opção desejada: ")
    return option


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função de menu do usuário
def menu_usuario(busca):
    os.system("clear||cls")
    conteudo = 40
    menu_opcoes = {
        "1": "Previsão do dia",
        "2": "Horoscopo",
        "3": "Numerologia",
        "4": "Configurar perfil",
        "0": "Sair"
    }
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Bem-vindo a PyTricia ' + busca['username'].split()[0]:^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Menu': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
        
    option = input("Digite a opção desejada: ")
    return option


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função que chama o menu do horoscopo
def horoscopo_menu():
    os.system("clear||cls")
    conteudo = 40
    menu_opcoes = {
        "1": "Horoscopo do dia",
        "0": "Voltar"
    }
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Horoscopo': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Menu': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    
    option = input("Digite a opção desejada: ")
    return option


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função para exibir a tela de mensagem do horoscopo
def horocopo_mensagem(astral, busca):
    conteudo = 60
    data_atual = datetime.date.today()
    data_formatada = data_atual.strftime('%d/%m/%Y')
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'A mensagem do dia ' + data_formatada + ' para o Signo de ' + busca['sign']:^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    linha_astral  = textwrap.wrap(astral, conteudo)
    for linha in linha_astral:
        print(f"|{linha:^{conteudo}}|")
    print(f"+{'-' * conteudo}+")    
    

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função para exibir o menu de numerologia
def numerologia_menu():
    os.system("clear||cls")
    conteudo = 40
    menu_opcoes = {
        "1": "Numerologia do Nome",
        "0": "Voltar"
    }
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Numerologia': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Menu': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    
    option = input("Digite a opção desejada: ")
    return option 


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função para exibir a numerologia do nome
def numerologia_nome_mensagem(nome, carta, definicao):
    valor_nome = verifica_numerologia(nome)
    conteudo = 60

    print(f"+{'-' * conteudo}+")
    print(f"|{'Valor numerológico do nome ' + nome + ': ' + str(valor_nome):^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{carta:^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    linhas_definicao = textwrap.wrap(definicao, conteudo)
    for linha in linhas_definicao:
        print(f"|{linha:^{conteudo}}|")
    print(f"+{'-' * conteudo}+")

    
    
# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função para exibir o menu de configurações do perfil
def menu_config_perfil():
    os.system("clear||cls")
    conteudo = 40
    menu_opcoes = {
        "1": "Ver perfil",
        "2": "Editar perfil",
        "3": "Excluir perfil",
        "0": "Voltar"
    }
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Configurações de perfil':^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Menu': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
        
    option = input("Digite a opção desejada: ")
    return option


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função para exibir a tela que exibe as previsões já realizadas
def previsoes_menu():
    os.system("clear||cls")
    conteudo = 40
    menu_opcoes = {
        "1": "Previsão para o dia",
        "2": "Histórico de previsões",
        "0": "Voltar"
    }
        
    print(f"+{'-' * conteudo}+")
    print(f"|{'Previsões feitas':^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Menu': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
        
    option = input("Digite a opção desejada: ")
    return option


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a tela onde será exibida a previsão do dia
def previsoes_mensagem(previsao, busca):
    conteudo = 60
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Previsão para o dia':^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    linha_astral  = textwrap.wrap(previsao, conteudo)
    for linha in linha_astral:
        print(f"|{linha:^{conteudo}}|")
    print(f"+{'-' * conteudo}+") 



def exibir_historico_menu(busca): 
    # Buscando o cpf do usuário e dizendo que esse será o "id"
    usuario_id = busca['cpf']
    
    # O nome do arquivo será "historico_usuario_cpf"
    arquivo_historico = f"historico/historico_usuario_{usuario_id}.json"
    
    # Verifica se existe algum dado histórico para ser exibido
    if not os.path.exists(arquivo_historico):
        print("Nenhum histórico encontrado.")
        return
    
    # Carrega o conteúdo do arquivo de histórico
    with open(arquivo_historico, "r") as arquivo:
        historico = json.load(arquivo) 
        
    # Exibe as previsões do histórico 
    
    conteudo = 60
    if not historico:
        print(f"+{'-' * conteudo}+")
        print(f"|{'Historico vazio':^{conteudo}}|")
        print(f"+{'-' * conteudo}+")
    else:
        print(f"+{'-' * conteudo}+")
        print(f"|{'Historico de previsões':^{conteudo}}|")
        print(f"+{'-' * conteudo}+")
        for previsao in historico:
            data_hora = previsao["data_hora"]
            previsao_texto = previsao["previsao"]
            linhas = textwrap.wrap(previsao_texto, conteudo - 2)
            # Exibir a data uma vez antes das linhas quebradas
            print(f"|{data_hora:^{conteudo}}|")
            for linha in linhas:
                print(f"|{linha:^{conteudo}}|")
            print(f"+{'-' * conteudo}+")
            
            
# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´