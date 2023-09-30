#12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

#Tabuada de 5: 

#5 X 1 = 5 

#5 X 2 = 10

#...

#5 X 10 = 50

num1 = 0
num2 = 0
resultado = 0

print("Informe o númeo que deseja ver a tabuada: ")
num1 = int(input())

match num1:

    case 1:

        print("Tabuada do {}:".format(num1))

        for i in range(1, 11):
            
            num2 += 1
            resultado = num1 * num2
            print("{} x {} = {}".format(num1, num2, resultado))
    
    case 2:

        print("Tabuada do {}:".format(num1))

        for i in range(1, 11):
            
            num2 += 1
            resultado = num1 * num2
            print("{} x {} = {}".format(num1, num2, resultado))
    
    case 3:

        print("Tabuada do {}:".format(num1))

        for i in range(1, 11):
            
            num2 += 1
            resultado = num1 * num2
            print("{} x {} = {}".format(num1, num2, resultado))
    
    case 4:

        print("Tabuada do {}:".format(num1))

        for i in range(1, 11):
            
            num2 += 1
            resultado = num1 * num2
            print("{} x {} = {}".format(num1, num2, resultado))

    case 5:

        print("Tabuada do {}:".format(num1))

        for i in range(1, 11):
            
            num2 += 1
            resultado = num1 * num2
            print("{} x {} = {}".format(num1, num2, resultado))

    case 6:

        print("Tabuada do {}:".format(num1))

        for i in range(1, 11):
            
            num2 += 1
            resultado = num1 * num2
            print("{} x {} = {}".format(num1, num2, resultado))

    case 7:

        print("Tabuada do {}:".format(num1))

        for i in range(1, 11):
            
            num2 += 1
            resultado = num1 * num2
            print("{} x {} = {}".format(num1, num2, resultado))
    
    case 8:

        print("Tabuada do {}:".format(num1))

        for i in range(1, 11):
            
            num2 += 1
            resultado = num1 * num2
            print("{} x {} = {}".format(num1, num2, resultado))

    case 9:

        print("Tabuada do {}:".format(num1))

        for i in range(1, 11):
            
            num2 += 1
            resultado = num1 * num2
            print("{} x {} = {}".format(num1, num2, resultado))

    case 10:

        print("Tabuada do {}:".format(num1))

        for i in range(1, 11):
            
            num2 += 1
            resultado = num1 * num2
            print("{} x {} = {}".format(num1, num2, resultado))
    
    case _:
        print("Erro: o valor deve ser de 1 a 10.")