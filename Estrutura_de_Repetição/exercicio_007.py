#7. Faça um programa que leia 5 números e informe o maior número.

num = 0
maior = 0

print("Informe 5 números:")
maior = int(input())

for num in range(1, 5):

    num = int(input())

    if num > maior:

        maior = num

print("Maior = {}".format(maior))