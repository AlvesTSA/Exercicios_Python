"""/*14. Faça um procedimento que lê 50 valores inteiros e retorna o maior e o menor deles.*/
"""
import random

def maior_menor():

    maior = -2147483648 # Inicializa o maior com o menor valor possível de um inteiro
    menor = 2147483648 # Inicializa o menor com o maior valor possível de um inteiro
    
    for i in range(0,50):
        
        valores = random.randint(0,10000) #usado para gerar numeros aleatórios e simular entrada do usuário.

        #valores = int(input()) Aqui, os valores de entrada foram substituidos por uma função que gera números aleatórios

        if (valores > maior):
        
            maior = valores 
        
        if (valores < menor):
        
            menor = valores
         
    return maior, menor

print("informe 50 valores inteiros: ")
    
mm = maior_menor()

print(f"Maior:{mm[0]}\nMenor: {mm[1]}")