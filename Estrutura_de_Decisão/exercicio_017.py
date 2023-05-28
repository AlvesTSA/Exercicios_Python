#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = 0

print("Informe um ano: ")
ano = int(input())

if ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):

    print("{} é um ano bissexto.".format(ano))

else:

    print("{} não é um ano bissexto.".format(ano))