import pickle
from logged import logged

def login(users):
    print("Login")
    cpf = input("Informe seu CPF: ")
    password = input("Senha: ")
    users = valid_login()
    
    if cpf in users and users[cpf]['password'] == password:
        logged()
    else:
        print("CPF ou senha invalidos")
        
def valid_login():
    try:
        with open("usuarios.dat", "rb") as arquivo:
            users_serialized = arquivo.read()
            users = pickle.loads(users_serialized)
    except FileNotFoundError:
        users = {}
    return users