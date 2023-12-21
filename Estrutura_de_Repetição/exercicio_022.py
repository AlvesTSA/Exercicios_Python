#22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

num = 0
divisivel = 0

num = int(input("Informe um número inteiro: "))

for i in range(1,num+1):

    resto = num % i

    if resto == 0:
        divisivel += 1

if divisivel > 2:

    print("Primo: Não")
    print("Divisível por: ")

    for i in range(1,num+1):

        resto = num % i

        if resto == 0:
            print(end="{} ".format(i))

else:
    print("Primo: Sim")
