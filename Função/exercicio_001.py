"""/*1. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.*/
"""
def Positivo_Negativo(num):

    if num > 0:
        return 'P'
    else:
        return 'N'

print("Informe um número inteiro: ")
num = int(input())
resposta = Positivo_Negativo(num)
print(f"Resposta: {resposta}")

