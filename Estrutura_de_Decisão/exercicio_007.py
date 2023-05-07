#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = 0
num2 = 0
num3 = 0
maior = 0
menor = 0

print("Informe três números: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3 :

    maior = num1

    if num2 < num3 :

        menor = num2

    else : 

        menor = num3

elif num2 > num1 and num2 > num3 :

    maior = num2

    if num1 < num3 :

        menor = num1

    else : 

        menor = num3

else : 

    maior = num3

    if num1 < num2 :

        menor = num1

    else : 

        menor = num2

print("Maior: " + str(maior) + "\nMenor: " + str(menor))

