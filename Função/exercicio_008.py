"""/*8. Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor booleano*/
"""

def impar_par(numero):
    return numero % 2 == 0

print(end="Informe um numero inteiro: ")
num = int(input())

if (impar_par(num)):
    print("O numero informado é PAR")
else:
    print("O numero informado é IMPAR")

