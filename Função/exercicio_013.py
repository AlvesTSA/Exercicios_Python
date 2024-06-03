"""/*13. Faça uma função que receba um valor inteiro e positivo e calcula o seu fatorial.*/
"""

def calcFatorial():

    fatorial = 1
 
    while True:
    
        num = int(input())

        if (num < 0):
        
            print("ERRO: o numero informado deve ser maior ou igual a zero.")
        else:
            break
           
    for i in range(2,num + 1):
    
        fatorial *= i
        
    return num,fatorial

print("Informe um numero inteiro e positivo: ")

fat = calcFatorial()

print(f"{fat[0]}! = {fat[1]}")