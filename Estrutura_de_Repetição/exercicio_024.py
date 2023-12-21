#24. Faça um programa que calcule o mostre a média aritmética de N notas.

n = int(input("Informe quantas notas deseja incluir: "))
soma = 0

for i in range(1, n+1):

    nota = float(input("Informe a nota {}: ".format(i)))

    soma += nota

media = soma / n

print("Nota media: {}".format(media))