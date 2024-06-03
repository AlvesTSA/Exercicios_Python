"""/*16. Faça uma função que recebe, por parâmetro, um valor inteiro e positivo e retorna o número de divisores desse valor.*/"""

def divisores(valor):

    count = 0

    for i in range(1,valor + 1):
    
        resto = valor % i

        if (resto == 0):
            count += 1
       
    return count

print(end="Informe um numero inteiro: ")
valor = int(input())

count = divisores(valor)

print(f"O valor informado e divisivel por {count} numeros.")