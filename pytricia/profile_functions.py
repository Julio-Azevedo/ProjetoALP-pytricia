# Funcionalidade de ver o perfil
def ver_perfil(search):
    print(f"Perfil do usuário")
    print(f"Nome do usuário: {search['username']}")
    print(f"Senha do usuário: {search['password']}")
    print(f"Data de nascimento do usuário: {search['birth']}")