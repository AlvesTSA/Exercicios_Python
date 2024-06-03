"""/*19. Faça um programa para imprimir:

1
1   2
1   2   3
.....
1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.*/
"""

def imprimir(n):

    for i in range(0,n+1):
    
        for j in range(1,i+1):
            print(end=f" {j}")
        print()

while True:

    print(end="Informe um valor inteiro: ")
    n = int(input())

    if (n <= 0): 
        print("Erro: o número deve ser inteiro e positivo.")
    else:
        break

imprimir(n)