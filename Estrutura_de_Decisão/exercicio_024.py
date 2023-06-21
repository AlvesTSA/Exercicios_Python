#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
 
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

import sys

saque = 0
nota1 = 0
nota5 = 0
nota10 = 0
nota50 = 0
nota100 = 0

print("Informe um valor de saque de ate 600 reais")
saque = int(input())

if(saque > 0 and saque <= 600):

    nota100 = saque // 100
    saque %= 100
    nota50 = saque // 50
    saque %= 50
    nota10 = saque // 10
    saque %= 10
    nota5 = saque // 5
    saque %= 5
    nota1 = saque

else: 

    print("Informe um valor de saque válido")

    sys.exit(0)

print("Nota de 100: {}\nNota de 50: {}\nNota de 10: {}\nNota de 5: {}\nNota de 1: {}".format(nota100, nota50, nota10, nota5, nota1))
