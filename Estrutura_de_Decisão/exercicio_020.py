#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é par ou ímpar e positivo ou negativo.

import sys

num1 = 0
num2 = 0
resultado = 0
op = 0

print("Informe dois números: ")
num1 = float(input())
num2 = float(input())
print("Escolha a operação\n\n[1]Adição\n[2]Subtração\n[3]Multiplicação\n[4]Divisão\n")
op = int(input())

match op:
    case 1:

        resultado = num1 + num2

    case 2:
        
        resultado = num1 - num2

    case 3:

        resultado = num1*num2

    case 4:

        if(num2 == 0):

            print("Não existe divisão por zero.")
            
            sys.exit(0) 

        else:

            resultado = num1/num2

    case _:

        print("Informe uma opção válida.")

        sys.exit(0)

if(resultado % 2 == 0):

    if(resultado > 0):

        print("Resultado: {} é par e positivo.".format(resultado))
    
    elif(resultado == 0):

        print("Resultado: {} é par e neutro.".format(resultado))

    else:

        print("Resultado: {} é par e negativo.".format(resultado))

else:

    if(resultado < 0):

        print("Resultado: {} é impar e negativo.".format(resultado))

    else:

        print("Resultado: {} é impar e positivo.".format(resultado))