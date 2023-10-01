#17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = 0
resultado = 0

print("Informe o valor que se deseja calcular o fatorial: ")
num = int(input())
resultado = num

print(end="{}! = {}".format(num, num))

while num > 1:

    num -= 1
    resultado *= num
    print(end=" x {}".format(num))

print(" = {}".format(resultado))