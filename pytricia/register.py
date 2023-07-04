import re as regex
from tinydb import TinyDB

# Criando o banco
db = TinyDB('users.json', indent = 4)

# Nomeando a tabela de usuário no banco
users = db.table('users')

def cadastro():
    # Processo de cadastro
    print("Iniciando processo de cadastro")
    
    username = input("Informe seu nome de usuário: ")
    while True:
        date = input("Informe sua data de nascimento: ")
        if valida_data(date):
            break
        else:
            print("Formato invalido, informe a data no formato dd/mm/aaaa")        
    password = input("Informe sua senha: ")

    # Criando o usuário
    user = {'username': username, 'password': password, 'birth': date}

    # Inserindo usuário no banco
    users.insert(user)
    
    print("Cadastro com sucesso!")

# Definando a função de validar o formato da data de nascimento
def valida_data(date):
    model = r"\d{2}/\d{2}/\d{4}"
    if regex.match(model, date):
        return True
    else:
        return False