#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax^2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
  
#Se o usuário informar o valor de A igual a zero. a equação não e do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
  
#Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;

#Se o delta calculado for igual a zero a equação possui apenas uma raiz real, informe ao usuário;

#Se o delta for positivo, a equação possui duas raízes reais, informe-as ao usuário;

import math

a = 0
b = 0
c = 0
delta = 0
x1 = 0
x2 = 0

print("Informe o valor de a: ")
a = float(input())

if (a != 0):
    
    print("Informe o valor de b: ")
    b = float(input())
    print("Informe o valor de c: ")
    c = float(input())

    delta = math.pow(b,2) - 4*a*c

    if (delta > 0):
        
        x1 = (- b + math.sqrt(delta))/2*a
        x2 = (- b - math.sqrt(delta))/2*a

        print("Valor de x': {}\nValor de x'': {}".format(x1, x2) )
        
    elif (delta == 0):
        
        x1 = (- b)/2*a
        x2 = (- b)/2*a

        print("Valor de x': {}\nValor de x'': {}".format(x1, x2))
    
    else:

        print("Os valores de x não são reais.")

else:

    print("A equação não é do segundo grau, informe um valor de 'a' diferente de zero")