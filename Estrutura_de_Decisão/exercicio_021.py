#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.Exemplo:326 = 3 centenas, 2 dezenas e 6 unidades

import sys

num = 0 
centena = 0
dezena = 0
unidade = 0

print("Informe um número inteiro de ate 999")
num = int(input())

if(num >= 0 and num < 1000):
 #Para obter a parte inteira da divisão, ou seja, o quociente inteiro, é necessário utilizar o operador de divisão inteira (//) em vez do operador de divisão (/).
    centena = num // 100   
    num %= 100
    dezena = num // 10
    num %= 10
    unidade = num
else:

    print("Informe um valor válido")

    sys.exit(0)

print("Centena: {}\nDezena: {}\nUnidade: {}".format(centena, dezena, unidade))

