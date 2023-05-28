#Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#Dicas:
 
#Três lados formam um triangulo quando a soma de quaisquer dos dois lados é maior que o terceiro; 
 
#Triângulo Equilátero: três lados iguais; 

#Triângulo Isósceles: quaisquer dois lados iguais;
 
#Triângulo Escaleno: três lados diferentes

lado_a = 0
lado_b = 0
lado_c = 0

print("Informe os lados do triângulo:")
lado_a = float(input())
lado_b = float(input())
lado_c = float(input())

if ((lado_a + lado_b) > lado_c and (lado_b + lado_c) > lado_a and (lado_a + lado_c) > lado_b and lado_a > 0 and lado_b > 0 and lado_c > 0):

    if (lado_a == lado_b and lado_a == lado_c and lado_b == lado_c):

        print("Triângulo equilátero")
        
    elif (lado_a == lado_b or lado_a == lado_c or lado_b == lado_c):
        
        print("Triângulo isósceles")

    elif (lado_a != lado_b and lado_a != lado_c and lado_b != lado_c):
        
        print("Triângulo escaleno")

else:

    print("Os valores informados não formam um triângulo, reinicie o programa e tente novamente.")