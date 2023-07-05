import os
from cadastro import db
from tinydb import Query
from perfil import perfil

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

usuarios = db.table('users')


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função de login de usuário
def login():
    os.system("clear||cls")
    conteudo = 40
    print(f"+{'-' * conteudo}+")
    print(f"|{'Login': ^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    
    # Processo de login
    login_nome = input("Infome seu nome de usuário: ")
    login_senha = input("Informe sua senha: ")
    
    # Consultando o banco 
    Usuario = Query()
    busca = usuarios.get((Usuario.username == login_nome) & (Usuario.password == login_senha))
    
    if busca is not None:
        os.system("clear||cls")
        perfil(busca)
    else:
        print("Usuário ou senha invalidos, você será redirecionando!")


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´