import os
# Função do menu do usuário logado 
def user_menu(search):
    os.system("clear||cls")
    print("=================================")
    print(f"= Bem vindo a PyTricia {search['username']} =")
    print("=================================")
    print("=     Selecione uma opção:      =")
    print("=================================")
    print("===  [1] - Horóscopo          ===")
    print("===  [2] - Numerologia        ===")
    print("===  [3] - Oráculo            ===")
    print("=================================")
    print()
    opt = input("Digite a opção desejada: ")
    return opt