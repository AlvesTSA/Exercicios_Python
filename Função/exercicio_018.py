"""/*18. Faça um programa para imprimir:

1
2   2
3   3   3
.....
n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.*/
"""

def imprimir(n):

    for i in range(0,n+1):
    
        for j in range(0,i):
            print(end=f" {i}")
        print()

while True:

    print(end="Informe um valor inteiro: ")
    n = int(input())

    if (n <= 0): 
        print("Erro: o número deve ser inteiro e positivo.")
    else:
        break

imprimir(n)