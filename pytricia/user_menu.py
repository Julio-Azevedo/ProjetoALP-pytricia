import os
# Função do menu do usuário logado 
def user_menu(search):
    os.system("clear||cls")
    print("=================================")
    print(f"= Bem vindo a PyTricia {search['username']} =")
    print("=================================")
    print("=     Selecione uma opção:      =")
    print("=================================")
    print("===  [1] - Ver perfil         ===")
    print("===  [2] - Editar perfil      ===")
    print("===  [3] - Previsão do dia    ===")
    print("=================================")
    print()
    opt = input("Digite a opção desejada: ")
    return opt