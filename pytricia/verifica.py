import os
import json
import random
import re as regex
from datetime import datetime
from unidecode import unidecode

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função que verifica se o nome do usuário é valido
def valida_nome(nome):
    # Usando unidecode para aceitar usernames com acentuação
    nome_valid = unidecode(nome)
    model = r"^[A-Za-z\s]+$"
    if regex.match(model, nome_valid):
        return True
    else:
        return False
    

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função que verifica se a data de nascimento é valida
def valida_idade(idade):
    modelo = r"^\d{2}/\d{2}/\d{4}$"
    if regex.match(modelo, idade):
        return True
    else:
        return False


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função que verifica se o cpf do usuário é valido
def valida_cpf(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    if len(cpf) != 11 or not cpf.isdigit():  
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0
        
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    if digito1 == int(cpf[9]) and digito2 == int(cpf[10]):
        return True
    else:
        return False



# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função que verifica o signo de um usuário
def verifica_signo(nascimento):
    dia, mes, ano = map(int, nascimento.split('/'))

    if (mes == 1 and 20 <= dia <= 31) or (mes == 2 and 1 <= dia <= 18):
        return "Aquário"
    elif (mes == 2 and 19 <= dia <= 29) or (mes == 3 and 1 <= dia <= 20):
        return "Peixes"
    elif (mes == 3 and 21 <= dia <= 31) or (mes == 4 and 1 <= dia <= 19):
        return "Áries"
    elif (mes == 4 and 20 <= dia <= 30) or (mes == 5 and 1 <= dia <= 20):
        return "Touro"
    elif (mes == 5 and 21 <= dia <= 31) or (mes == 6 and 1 <= dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and 21 <= dia <= 30) or (mes == 7 and 1 <= dia <= 22):
        return "Câncer"
    elif (mes == 7 and 23 <= dia <= 31) or (mes == 8 and 1 <= dia <= 22):
        return "Leão"
    elif (mes == 8 and 23 <= dia <= 31) or (mes == 9 and 1 <= dia <= 22):
        return "Virgem"
    elif (mes == 9 and 23 <= dia <= 30) or (mes == 10 and 1 <= dia <= 22):
        return "Libra"
    elif (mes == 10 and 23 <= dia <= 31) or (mes == 11 and 1 <= dia <= 21):
        return "Escorpião"
    elif (mes == 11 and 22 <= dia <= 30) or (mes == 12 and 1 <= dia <= 21):
        return "Sagitário"
    elif (mes == 12 and 22 <= dia <= 31) or (mes == 1 and 1 <= dia <= 19):
        return "Capricórnio"
    else:
        return "Data de nascimento inválida"


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´


# Criando função que verifica a mensagem do dia de acordo com o signo
def verifica_horoscopo():
    with open('horoscopo.json') as arquivo:
        dados = json.load(arquivo)
        # A variável "frases" está armazenando um dicionario
        frases = dados['phrases']
        # "astral" está selecionando uma frase aleatória com a função choice do random, nesta parte, estão sendo pegos os valores da variavel "frases", e então é utilizado a função 'list', para colocalo em lista, e o "['phrase']", garante que acessamos a chave do objeto para obter a frase
        astral = random.choice(list(frases.values()))['phrase']
        return astral 
    
    
# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função que verifica o valor numerologico do nome do usuário
def verifica_numerologia(nome):
    tabela = {
        '1': ['A', 'J', 'S'],
        '2': ['B', 'K', 'T'],
        '3': ['C', 'L', 'U'],
        '4': ['D', 'M', 'V'],
        '5': ['E', 'N', 'W'],
        '6': ['F', 'O', 'X'],
        '7': ['G', 'P', 'Y'],
        '8': ['H', 'Q', 'Z'],
        '9': ['I', 'R']
    }
    
    nome
    valor = 0
    for letra in nome:
        for chave, letras in tabela.items():
            if letra in letras:
                valor += int(chave)
                break
        if valor > 36:
            valor = valor % 36
    return valor

    
# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função que verifica a mensagem de acordo com o valor nome do usuário
def definicao_numerologia(numero):
    with open('sentenças.json') as arquivo:
        dados = json.load(arquivo)
        
    lenormand = dados.get("lenormand")
    if lenormand:
        carta = lenormand.get(str(numero))
        if carta:
            return carta["carta"], carta["significado"]
    
    return None, None


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´   

# Criando função que verifica a mensagem do dia para certo usuário
def verifica_previsao():
    with open('horoscopo.json') as arquivo:
        dados = json.load(arquivo)
        frases = dados['phrases']
        previsao = random.choice(list(frases.values()))['phrase']
        return previsao
    

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função que salva o historico de previsões
def salvar_historico(busca, previsao):
    # 
    usuario_id = busca['cpf']
    
    # Cria a pasta historico se não existir
    historico = "historico"
    if not os.path.exists(historico):
        os.makedirs(historico)
        
    arquivo_historico = f"{historico}/historico_usuario_{usuario_id}.json"
    
    if not os.path.exists(arquivo_historico):
        with open(arquivo_historico, "w") as arquivo:
            json.dump([], arquivo)
            
    with open(arquivo_historico, "r") as arquivo:
        historico = json.load(arquivo)
        
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    historico.append({"data_hora": data_hora, "previsao": previsao})
    
    with open(arquivo_historico, "w") as arquivo:
        json.dump(historico, arquivo)


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´