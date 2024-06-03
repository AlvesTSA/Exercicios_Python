"""/*17. Escreva uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o somatório desse valor.*/
"""

def somatorio(n):

    soma = 0

    for i in range(1,n+1):
        soma += i
    
    return soma

while True:

    print(end="Informe um valor inteiro: ")
    n = int(input())

    if (n <= 0): 
        print("Erro: o número deve ser inteiro e positivo.")
    else:
        break

soma = somatorio(n)

print(f"Somatório de {n}: {soma}")