"""/*2. Leia uma matriz 6 x 6, conte e escreva quantos valores maiores que 10 ela possui.*/"""

import random

size = 6
matriz = []

for i in range(size):
    l = []
    for j in range(size):
        l.append(0)
    
    matriz.append(l)

max = 30
min = 1

for i in range(size):
    for j in range(size):
        matriz[i][j] = random.randint(min,max)

count = 0

print("Matriz lida: ")
for i in range(size):
    for j in range(size):
        print(end=f"{matriz[i][j]} ")

        if matriz[i][j] > 10:
            count += 1

    print()

print(f"Existem {count} valores maiores que 10.")
