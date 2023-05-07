# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto_a = 0
produto_b = 0
produto_c = 0
barato = 0

print("Informe o preço de três produtos: ")
produto_a = float(input())
produto_b = float(input())
produto_c = float(input())

if produto_a < produto_b and produto_a < produto_c :

    barato = produto_a

elif produto_b < produto_a and produto_b < produto_c :

    barato = produto_b

else :

    barato = produto_c

print("Mais barato: " + str(barato))

