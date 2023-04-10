#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_Hora = float(input('Digite quantos você ganha por hora R$:  '))

horas_mes = float(input('Digite quantas horas você trabalhou nesse mês  '))

salario = ganho_Hora*horas_mes

print('Seu salário é {} reais.' .format(salario))