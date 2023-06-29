import re as regex
import pickle

# função de cadastrar usuários
def register(users):
    print("Iniciando processo de cadastro")
    username = input("Informe seu nome: ")
    while True:
        date = input("Informe sua data de nascimento: ")
        if valid_date(date):
            break
        else:
            print("Formato inválido, informe sua data de nascimento como dd/mm/aaaa")
    password = input("Informe sua senha: ")
    while True:
        cpf = input("Informe seu CPF: ")
        if cpf not in users:
            break
        else:
            print("Há um usuário já cadastrado com esse CPF")
          
    user = {
        'username': username,
        'birth': date,
        'password': password,
        'cpf': cpf
    }

    users[cpf] = user
    save_user(users)
    print("Cadastrado com sucesso!")

# função que valida a data inserida   
def valid_date(date):
    model = r"\d{2}/\d{2}/\d{4}"
    if regex.match(model, date):
        return True
    else:
        return False
    
def save_user(users):
    with open("users.dat", "ab") as arquivo:
        users_printed = pickle.dumps(users)
        arquivo.write(users_printed)
