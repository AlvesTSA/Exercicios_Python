# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a)o produto do dobro do primeiro com metade do segundo .
# b)a soma do triplo do primeiro com o terceiro.
# c)o terceiro elevado ao cubo.        

num1 = 0 
num2 = 0 
num3 = 0
produto = 0
soma = 0
cubo = 0

print("informe o primeiro número: ")
num1 = float(input())

print("informe o segundo número: ")
num2 = float(input())

print("Informe o terceiro número: ")
num3 = float(input())

produto = 2*num1*(num2/2)
soma = 3*num1 + num3
cubo = num3*num3*num3

print("O produto do dobro do primeiro com metade do segundo: {}" .format(produto))
print("A soma do triplo do primeiro com o terceiro:{}" .format(soma))
print("O terceiro elevado ao cubo: {}" .format(cubo))
