#18. . Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = 0
num = 0
menor = 0
maior = 0
soma = 0

print(end="Informe quantos numeros deseja incluir: ")
n = int(input())
print("Informe os números:")
num = int(input())

maior = num
menor = num
soma = num

for i in range(1, n):

    num = int(input())
    soma += num

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print("Maior: {}\nMenor: {}\nSoma: {}".format(maior, menor, soma))