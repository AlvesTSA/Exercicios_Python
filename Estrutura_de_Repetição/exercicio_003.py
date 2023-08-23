#3. Faça um programa que leia e valide as seguintes informações:
 
#Nome: maior que 3 caracteres; 
 
#Idade: entre 0 e 150; 

#Salário: maior que zero;

#Sexo: 'f' ou 'm';

#Estado Civil: 's', 'c', 'v', 'd';

nome = ''
idade = 0
salario = 0
sexo = ''
estado_civil = ''

while True:

    print("Informe seu nome:")
    nome = input()

    if len(nome) > 3:
        print("Nome atribuido com sucesso.")
        break
    else:
        print("Informe um nome com mais de três caracteres.")

while True:

    print("Informe sua idade:")
    idade = int(input())

    if idade > 0 and idade < 150:
        print("Idade atribuido com sucesso.")
        break
    else:
        print("ERROR: informe uma idade válida.")

while True:

    print("Informe seu salario:")
    salario = float(input())

    if salario > 0:
        print("Salário atribuido com sucesso.")
        break
    else:
        print("ERROR: salário inválido..")

while True:

    print("Informe seu sexo:")
    sexo = input()

    if sexo == 'm' or sexo == 'f' :
        print("Sexo atribuido com sucesso.")
        break
    else:
        print("ERROR: informe m ou f")

while True:

    print("Informe seu estado civil:")
    estado_civil = input()

    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        print("Estado civil atribuido com sucesso.")
        break
    else:
        print("ERROR: responda com s, c, v, ou d.")