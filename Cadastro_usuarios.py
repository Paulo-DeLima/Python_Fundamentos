usuarios = {}
print("Bem-vindo ao sistema de cadastro de usuários!")
print("Digite os dados do usuário a ser cadastrado:")

while True:
    nome = input("Nome:")
    senha = input("Senha:")
    while len(senha) < 6:
        print("A senha deve ter pelo menos 6 caracteres. Digite novamente:")
        senha = input("Senha:")
    usuarios[nome] = senha
    cont = input ("Deseja cadastrar outro usuário? (s/n): ")
    if cont.lower() != 's':
        break

while True:
     print("Deseja visualizar os usuários cadastrado? (s/n): ")
     if (resposta := input().lower()) == 's':
         print("Usuários Cadastrados:")
         for user, senha in usuarios.items():
             print(f"Usuário: {user} | Senha: {senha}")

     else:
         print("Saindo do sistema de cadastro.")
         break