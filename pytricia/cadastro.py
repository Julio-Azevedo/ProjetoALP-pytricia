import os
from tinydb import TinyDB
from verifica import valida_nome, valida_idade, verifica_signo, valida_cpf


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´


# Criando o arquivo json onde ficaram salvos os usuários
db = TinyDB('users.json', indent = 5)

# Nomeando a tabela de usuário no banco
usuarios = db.table('users')


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função de cadastro
def cadastro():
    os.system("clear||cls")
    conteudo = 40
    print(f"+{'-' * conteudo}+")
    print(f"|{'Cadastro': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    
    while True:
        nome = input("Informe seu nome: ")
        if valida_nome(nome):
            break
        else:
            print("Nome invalido, Tente novamente!")
    while True:
        idade = input("Informe sua data de nascimento: ")
        if valida_idade(idade):
            break
        else:
            print("Formato invalido, informe a data no formato dd/mm/aaaa")
    while True:
        cpf = input("Informe seu CPF: ")
        if valida_cpf(cpf):
            break
        else:
            print("Nome invalido, Tente novamente!")
    senha = input("Informe sua senha: ")
    
    signo = verifica_signo(idade)
    
    # Colocando os dados do usuário em um dicionario
    user = {
        'username': nome,
        'age': idade,
        'cpf': cpf,
        'password': senha,
        'sign': signo
    }
    
    # Inserindo o usuário no banco
    usuarios.insert(user)
    
    print("Cadastrado com sucesso!")

 
# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´