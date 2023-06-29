import os
from register import db
from tinydb import Query
from register import valid_date

users = db.table('users')

def edit_profile(search, username, edited):
    # Exibindo perfil atual do usuário
    os.system("clear||cls")
    print(f"Dados atuais")
    print(f"Nome do usuário: {search['username']}")
    print(f"Senha do usuário: {search['password']}")
    print(f"Data de nascimento do usuário: {search['birth']}")
    
    edited = True
    while edited:
        choose = input("Deseja mesmo editar seu perfil? (yes / not): ")
        if choose == "not" or choose == "n":
            print("Dados inalterados")
            break
        else:
            os.system("clear||cls")
            print("Editando perfil")
            
            # Consultado perfil no banco de dados
            User = Query()
            edit_user = users.get(User.username == username)
            
            if edit_user is not None:
                # Pedindo os novos dados
                new_username = input("Informe o novo nome: ")
                new_password = input("Informe sua nova senha: ")
                opt_date = input(f"Deseja alterar a data de nascimento? atual: {search['birth']} (yes / not): ")
                if opt_date == "yes" or opt_date == "y":
                    while True:
                        new_date = input("Informe nova data: ")
                        if valid_date(new_date):
                            break
                        else:
                            print("Formato invalido, informe a data no formato dd/mm/aaaa")
                else:
                    new_date = edit_user['birth']
                
                # Atualizando os dados
                if new_username:
                    edit_user['username'] = new_username
                if new_password:
                    edit_user['password'] = new_password
                if new_date:
                    edit_user['birth'] = new_date
                    
                # Salvando
                users.update(edit_user, User.username == username)
                
                print("Perfil atualizado com sucesso!")
                print("Você será deslogado")
                edited = False
                break
            else:
                print("Ocorreu um erro na atualização de perfil, tente novamente")
                break