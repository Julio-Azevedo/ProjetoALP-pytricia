from register import db
from tinydb import Query

def login():
    # Iniciando processo de login
    print("Login")
    username = input("Informe seu nome de usuário: ")
    password = input("Informe sua senha: ")
    # Consultando o banco de dados
    user = Query()
    search = db.search((user.username == username) & (user.password == password))
    
    if search:
        print("Sucesso")
    else:
        print("Usuário ou senha inválidos")