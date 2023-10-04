#20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

num = 0
resultado = 0
op = 0

while True:

    print("Informe o valor que se deseja calcular o fatorial: ")

    while True:
        num = int(input())
    
        if num <= 0 or num >= 16:

            print("Erro: informe um valor de 1 a 15.")
        else:
            break
            
    resultado = num

    print(end="{}! = {}".format(num, num))

    while num > 1:

        num -= 1
        resultado *= num
        print(end=" x {}".format(num))

    print(" = {}".format(resultado))

    print(end="Informe 1 para continuar ou 0 para sair: ")
    op = int(input())

    if op == 1:
        op = 1
    elif op == 0:
        break