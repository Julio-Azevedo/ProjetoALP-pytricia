from tinydb import TinyDB

db = TinyDB('users.json')

def register():
    # Processo de cadastro
    print("Iniciando processo de cadastro")
    username = input("Informe seu nome de usuário: ")
    password = input("Informe sua senha: ")
    
    # Criando o usuário
    user = {'username': username, 'password': password}

    # Inserindo usuário no banco
    db.insert(user)
    
    print("Cadastro com sucesso!")