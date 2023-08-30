#9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

num = 0

for i in range(1, 51):

    num += 1
    resto = num % 2

    if resto != 0 and num != 1:

        print("{}".format(num))
