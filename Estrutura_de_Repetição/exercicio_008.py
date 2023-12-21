#8. Faça um programa que leia 5 números e informe a soma e a média dos números.

num = 0
soma = 0
media = 0
i = 0

print("Informe 5 números:")

for i in range(1, 6):

    num = float(input())
    soma += num

media = soma/i

print("Soma = {}\nMedia = {}".format(soma, media))