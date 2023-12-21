#23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

num = 0
divisoes = 0

num = int(input("Informe um número inteiro como limite de intervalo de numeros primos: "))
print(end="Numeros primos no intervalo de 1 a {}: ".format(num))

for i in range(1,num+1):

    divisivel = 0

    for y in range(1,i+1):

        resto = i % y
        divisoes += 1

        if resto == 0:
            divisivel += 1

    if divisivel < 3:
        print(end="{} ".format(i))
   
