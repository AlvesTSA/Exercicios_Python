"""/*5. Leia duas matrizes 20 x 20 e escreva os valores da primeira que ocorrem em qualquer posição da segunda.*/"""

import random

size = 20
intervalo_max = 1000
intervalo_min = 1
matrizA = [[0 for _ in range(size)] for _ in range(size)]
matrizB = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):

    for j in range(size):
        
        
        matrizA[i][j] = random.randint(intervalo_min,intervalo_max)
        matrizB[i][j] = random.randint(intervalo_min,intervalo_max)

print("Todos os valores da matriz A que estao na matriz B\n")

for i in range(size):

    for j in range(size):
    
        for w in range(size):

            for z in range(size):
            
                if (matrizA[i][j] == matrizB[w][z]):
                        
                    print(end=f"{matrizA[i][j]} ")