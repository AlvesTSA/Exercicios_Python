"/*9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.*/"

vetor = []
soma = 0

print("Iinforme 10 númeors inteiros:")

for i in range(0, 10):

    a = int(input())
    vetor.append(a)

    soma = soma + (vetor[i]*vetor[i])

print(f"Soma dos quadrados: {soma}")