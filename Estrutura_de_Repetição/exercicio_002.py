#2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

senha = ''
nome = ''

while True:

    print("Informe um nome de usuário: ")
    nome = input()
    print("Informe uma senha: ")
    senha = input()

    if nome != senha :
        print("cadastro realizado com sucesso.")
        break
    else:
        print("ERROR: nome e senha devem ser diferentes.")
