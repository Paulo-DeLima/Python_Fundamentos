usuarios = {}
print("Bem-vindo ao sistema de cadastro de usuários!")
print("Digite os dados do usuário a ser cadastrado:")

while True:
    nome = input("Nome:")
    senha = input("Senha:")
    usuarios[nome] = senha

    cont = input ("Deseja cadastrar outro usuário? (s/n): ")
    if cont.lower() != 's':
        break


print("Usuários Cadastrados:")
for user, senha in usuarios.items():
    print(f"Usuário: {user} | Senha: {senha}")