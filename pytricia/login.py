import os
from register import db
from tinydb import Query

users = db.table('users')

def login():
    print("Login")
    # Iniciando processo de login
    username = input("Informe seu nome de usuário: ")
    password = input("Informe sua senha: ")
    # Consultando o banco de dados
    User = Query()
    search = users.get((User.username == username) & (User.password == password))
        
    if search is not None:
        os.system("clear||cls")
        logged(search)
    else:
        print("Usuário ou senha inválidos")
        
def logged(search):
    print(f"Bem vindo a PyTricia {search['username']}")