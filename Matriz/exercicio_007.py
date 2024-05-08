"""/*7. Leia duas matrizes 4 x 4 e escreva uma terceira com os 4 maiores elementos entre as primeiras*/"""

import random

size = 4
max = 100
min = 1
matrizA = [[0 for _ in range(size)] for _ in range(size)]
matrizB = [[0 for _ in range(size)] for _ in range(size)]
maiores = [0 for _ in range(size*size + size*size)] # Vamos armazenar os maiores valores de ambas as matrizes aqui
k = 0 # indice para percorrer o array de maiores valores
matrizResultante = [[0 for _ in range(size)] for _ in range(size)]# Matriz para armazenar os 4 maiores valores

print("Informe os elementos da matriz A:")

for i in range(size):
    for j in range(size):
        matrizA[i][j] = random.randint(min,max)
        maiores[k] = matrizA[i][j]
        k += 1
        print(end=f"{matrizA[i][j]} ")
    
    print()

print("Informe os elementos da matriz B:")

for i in range(size):
    for j in range(size):
        matrizB[i][j] = random.randint(min,max)
        maiores[k] = matrizB[i][j]
        k += 1
        print(end=f"{matrizB[i][j]} ")
    
    print()

# Ordenar os maiores valores em ordem decrescente
for i in range(size*size + size*size):
    for j in range(size*size + size*size):

        if(maiores[i] > maiores[j]):
            temp = maiores[i]
            maiores[i] = maiores[j]
            maiores[j] = temp

print("Matriz resultante:")
# Preencher a matriz resultante com os 4 maiores valores
for i in range(size):
    for j in range(size):
        matrizResultante[i][j] = maiores[j]
        print(end=f"{matrizResultante[i][j]} ")
    
    print()
