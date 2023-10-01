#14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

num = 0
impar = 0
par = 0
resto = 0

print("Informe 10 números inteiros:")

for i in range(1, 11):

    num = int(input())
    resto = num % 2

    if resto == 0:
        par += 1
    else:
        impar += 1

print("Quantidade de impar: {}".format(impar))
print("Quantidade de par: {}".format(par))
