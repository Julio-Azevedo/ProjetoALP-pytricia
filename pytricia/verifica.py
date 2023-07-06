import re as regex
import json
import random

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função que verifica se o nome do usuário é valido
def valida_nome(nome):
    model = r"^[A-Za-z\s]+$"
    if regex.match(model, nome):
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
def valida_cpf():
    pass


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


# Criando função que verifica a mensagem do dia para certo usuário
def verifica_horoscopo():
    with open('horoscopo.json') as arquivo:
        dados = json.load(arquivo)
        # A variável "frases" está armazenando um dicionario
        frases = dados['phrases']
        # "astral" está selecionando uma frase aleatória com a função choice do random, nesta parte, estão sendo pegos os valores da variavel "frases", e então é utilizado a função 'list', para colocalo em lista, e o "['phrase']", garante que acessamos a chave do objeto para obter a frase
        astral = random.choice(list(frases.values()))['phrase']
        return astral 
    
    
# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função que verifica a mensagem de acordo com o nome do usuário
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
        if valor >= 36:
            valor = valor % 36
    return valor

    

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´