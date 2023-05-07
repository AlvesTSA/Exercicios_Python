# . Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = 0
num2 = 0
num3 = 0
maior1 = 0
maior2 = 0
maior3 = 0

print("Informe três números: ")
num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3 :

    maior1 = num1

    if num2 > num3 :

        maior2 = num2
        maior3 = num3

    else : 

        maior2 = num3
        maior3 = num2

elif num2 > num1 and num2 > num3 :

    maior1 = num2

    if num1 > num3 :

        maior2 = num1
        maior3 = num3

    else : 

        maior2 = num3
        maior3 = num1

else :

    maior1 = num3

    if num1 > num2 :

        maior2 = num1
        maior3 = num2

    else : 

        maior2 = num2
        maior3 = num1

print("Ordem decrescente: \n" + str(maior1) + "\n" + str(maior2) + "\n" + str(maior3))