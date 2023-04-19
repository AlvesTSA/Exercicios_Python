#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a)Para homens: (72.7*h) - 58
# b)Para mulheres: (62.1*h) - 44.7  

h = 0
peso_mulher = 0
peso_homem = 0 

print("Informe sua altura: ")
h = float(input())

peso_mulher = (62.1*h) - 44.7
peso_homem = (72.7*h) - 58

print("O peso ideal para mulheres: {}".format(peso_mulher))
print("O peso ideal para homens: {}".format(peso_homem))

