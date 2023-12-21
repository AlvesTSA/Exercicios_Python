#21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = 0
divisivel = 0

num = int(input("Informe um número inteiro: "))

for i in range(1,num+1):

    resto = num % i

    if resto == 0:
        divisivel += 1

if divisivel > 2:
    print("Primo: Não")
else:
    print("Primo: Sim")
