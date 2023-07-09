import os
from cadastro import db
from verifica import valida_nome, valida_idade, verifica_signo

# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função para ver as informações do perfil
def exibir_perfil(busca):
    conteudo = 40
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Informações do perfil':^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Nome de usuário: '+busca['username']:{conteudo}}|")
    print(f"+{'-' * conteudo}+") 
    print(f"|{'Data de nascimento: '+busca['age']:{conteudo}}|")
    print(f"+{'-' * conteudo}+") 
    print(f"|{'CPF: '+busca['cpf']:{conteudo}}|")
    print(f"+{'-' * conteudo}+") 
    print(f"|{'Senha: '+busca['password']:{conteudo}}|")
    print(f"+{'-' * conteudo}+") 


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando função para editar perfil
def editar_perfil(busca):
    conteudo = 40
    usuarios = db.table('users')
    option = editar_perfil_menu()
    while option != "0":
        # Editando nome do usuário
        if option == "1":
            os.system("clear||cls")
            print(f"+{'-' * conteudo}+")
            print(f"|{'Editando nome de usuário':^{conteudo}}|")
            print(f"+{'-' * conteudo}+")
            while True:
                novo_username = input("Digite o novo nome de usuário: ")
                busca['username'] = novo_username
                if valida_nome(novo_username):
                    break
                else:
                    print("Nome invalido, Tente novamente!")
            usuarios.update({'username': novo_username}, doc_ids=[busca.doc_id])
            os.system("clear||cls")
            print("Nome de usuário atualizado com sucesso!")
            
        # Editando a data de nascimento do usuário
        elif option == "2":
            os.system("clear||cls")
            print(f"+{'-' * conteudo}+")
            print(f"|{'Editando data de nascimento':^{conteudo}}|")
            print(f"+{'-' * conteudo}+")
            while True:
                nova_data_nascimento = input("Digite a nova data de nascimento: ")
                busca['age'] = nova_data_nascimento
                if valida_idade(nova_data_nascimento):
                    novo_signo = verifica_signo(nova_data_nascimento)
                    break
                else:
                    print("Nome invalido, Tente novamente!")
            usuarios.update({'age': nova_data_nascimento}, doc_ids=[busca.doc_id])
            usuarios.update({'sign':novo_signo}, doc_ids=[busca.doc_id])
            os.system("clear||cls")
            print("Data de nascimento atualizada com sucesso!")
            
        # Editando a senha do usuário
        elif option == "3":
            os.system("clear||cls")
            nova_senha = input("Digite a nova senha: ")
            busca['password'] = nova_senha
            usuarios.update({'password': nova_senha}, doc_ids=[busca.doc_id])
            print("Senha atualizada com sucesso!")
        else:
            print("Opção inválida, tente novamente!")
        option = editar_perfil_menu()


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

def editar_perfil_menu():
    conteudo = 40
    menu_opcoes = {
        "1": "Nome de usuário",
        "2": "Data de nascimento",
        "3": "Senha",
        "0": "Voltar"
    }
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Editar perfil':^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Opções de edição':^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    for i, j in menu_opcoes.items():
        print(f"|{f' {i} - {j}':{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    
    option = input("Digite a opção desejada: ")
    return option


# ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´

# Criando a função de excluir o perfil
def deletar_perfil(busca):
    conteudo = 40
    usuarios = db.table('users')
    
    print(f"+{'-' * conteudo}+")
    print(f"|{'Exclusão de perfil':^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Suas informações':^{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Nome de usuário: '+busca['username']:{conteudo}}|")
    print(f"+{'-' * conteudo}+") 
    print(f"|{'Data de nascimento: '+busca['age']:{conteudo}}|")
    print(f"+{'-' * conteudo}+") 
    print(f"|{'CPF: '+busca['cpf']:{conteudo}}|")
    print(f"+{'-' * conteudo}+")
    print(f"|{'Senha: '+busca['password']:{conteudo}}|")
    print(f"+{'-' * conteudo}+") 
    
    confirm = input("Tem certeza que deseja excluir sua conta? (S/N): ")
    
    if confirm.lower() == "s":
        usuarios.remove(doc_ids=[busca.doc_id])
        print("Conta excluída com sucesso!")
        return True
    else:
        print("Operação cancelada.")
        return False