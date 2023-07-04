import os
# Definindo a função do menu principal
def menu_principal():
    os.system("clear||cls")
    print("=============================")
    print("===       PyTricia        ===")
    print("=============================")
    print("=   Selecione uma opção:    =")
    print("=============================")
    print("===  [1] - Entrar         ===")
    print("===  [2] - Cadastrar      ===")
    print("===  [0] - Sair           ===")
    print("=============================")
    print()
    print("\tAluno: Júlio César Costa de Azevedo")
    print()
    opt = input("Digite a opção desejada: ")
    return opt