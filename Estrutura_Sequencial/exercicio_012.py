#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = 0
peso = 0 

print("Informe sua altura: ")
altura = float(input())

peso = (72.7*altura) - 58

print("O peso ideal: {}" .format(peso))
