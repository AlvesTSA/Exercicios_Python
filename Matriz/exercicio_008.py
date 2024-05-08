"""/*8. Leia uma matriz 8x 8 e escreva o maior elemento da diagonal principal e a soma dos elementos da diagonal secundaria.*/
"""

import random

size = 8
max = 100
min = 0
matriz = [[0 for _ in range(size)] for _ in range(size)]
maior = 0

print(f"Informe uma matriz {size} x {size}: ")

for i in range(size):
    
    for y in range(size):
        
        matriz[i][y] = random.randint(min,max)

#maior valor da diagonal principal
maior = matriz[0][0]

for i in range(size):
    
    if(matriz[i][i] > maior):
        
        maior = matriz[i][i]

#soma da diagonal secundária
soma = 0
j = size - 1

for i in range(size):
    
    soma += matriz[i][j]
    j -= 1

print("\nMatriz lida:\n")

for i in range(size):
    
    for y in range(size):
        
        print(end=f"{matriz[i][y]} ")
    
    
    print()

print(end="Diagonal principal: ")

for i in range(size):
    
    print(end=f"{matriz[i][i]} ")

print(end=f"\nMaior valor da diagonal principal: {maior}")
print(end=f"\nDiagonal secundaria: ")
j = size - 1

for i in range(size):
    
    print(end=f"{matriz[i][i]} ")
    j -= 1

print(end=f"\nSoma da diagonal secundaria: {soma}")
