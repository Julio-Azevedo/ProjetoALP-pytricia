import os
import random
import datetime
import json

# Funcionalidade de horóscopo
def horos():
    os.system("clear||cls")
    print("========================================")
    print("===            Horóscopo             ===")
    print("========================================")
    print("=         Selecione uma opção:         =")
    print("========================================")
    print("===  [1] - Horóscopo de hoje         ===")
    print("===  [2] - Horóscopo de amanhã       ===")
    print("===  [3] - Horóscopo da semana       ===")
    print("===  [0] - Voltar                    ===")
    print("========================================")
    print()
    opt = input("Digite a opção desejada: ")
    
    if opt == "1":
        with open('horoscope.json') as arquivo:
            dados = json.load(arquivo)
            # A variável "frases" está armazenando um dicionario
            frases = dados['phrases']
            # "astral" está selecionando uma frase aleatória com a função choice do random, nesta parte, estão sendo pegos os valores da variavel "frases", e então é utilizado a função 'list', para colocalo em lista, e o "['phrase']", garante que acessamos a chave do objeto para obter a frase
            astral = random.choice(list(frases.values()))['phrase']
        print(f"Astral do dia: {datetime.date.today()}")
        print(f"Frase do horóscopo: {astral}")
        
    elif opt == "2":
        with open('horoscope.json') as arquivo:
            dados = json.load(arquivo)
            frases = dados['phrases']
            astral = random.choice(list(frases.values()))['phrase']
        print(f"Astral do dia: {datetime.date.today() + datetime.timedelta(days=1)}")
        print(f"Frase do horóscopo: {astral}")
        
    elif opt == "3":
        with open('horoscope.json') as arquivo:
            dados = json.load(arquivo)
            frases = dados['phrases']
            astral = random.choice(list(frases.values()))['phrase']
        print(f"Astral da Semana: {datetime.date.today()}")
        print(f"Frase do horóscopo: {astral}")

    
# Funcionalidade de ver o perfil
def ver_perfil(search):
    print(f"Perfil do usuário")
    print(f"Nome do usuário: {search['username']}")
    print(f"Senha do usuário: {search['password']}")
    print(f"Data de nascimento do usuário: {search['birth']}")