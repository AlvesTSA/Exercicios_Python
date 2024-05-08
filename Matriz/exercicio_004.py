"""/*4. Leia uma matriz 4 x 4 e troque os valores da 1ª.linha pelos da 4ª.coluna, vice-e-versa. Escrever ao final a matriz obtida */"""

import random

size = 4
max = 9
min = 1
matriz = []
temp = 0

for i in range(size):
    l = []
    for j in range(size):
        l.append(0)
    
    matriz.append(l)

for i in range(size):

    for j in range(size):
    
        matriz[i][j] = random.randint(min,max)

print("Matriz lida: ")

for i in range(size):

    for j in range(size):
        
        print(end=f"{matriz[i][j]} ")

    print()

for i in range(size):

    temp = matriz[0][i]
    matriz[0][i] = matriz[i][3]
    matriz[i][3] = temp

print("Matriz invertida: ")

for i in range(size):

    for j in range(size):
    
        print(end=f"{matriz[i][j]} ")

    print()