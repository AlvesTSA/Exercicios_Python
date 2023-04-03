#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

C = float(input('Digite a temperatura em Celsius:  '))

F = 1.8*C + 32

print('A temperatura em Fahrenheit é: {:.2f}°' .format(F))