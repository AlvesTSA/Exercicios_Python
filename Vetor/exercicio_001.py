"1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os."

vetor = []

print("Informe 5 números inteiros")

for i in range(0, 5):

    num = int(input("Informe o {}: ".format(i + 1)))
    vetor.append(num)

print("Valores lidos: ")

for i in range(0, 5):

    print(end="{} ".format(vetor[i]))
