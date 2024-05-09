"""/*19. Leia duas matrizes 10 x 10 e faça uma substituição entre a diagonal inferior da primeira coma diagonal superior da segunda.*/"""

import random

size = 10
max = 10
min = 0
matrizA = [[0 for _ in range(size)] for _ in range(size)]
matrizB = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):

    for j in range(size):
        
        matrizA[i][j] = random.randint(min,max)
        matrizB[i][j] = random.randint(min,max)
    
print("Matrizes originais:")
for i in range(size):
    
    for j in range(size):
        
        print(end=f"{matrizA[i][j]} ")
    
    print()

print()

for i in range(size):
    
    for j in range(size):
        
        print(end=f"{matrizB[i][j]} ")
    
    print()

temp = 0

for i in range(size):
    
    for j in ((i + 1),size):
        
        temp = matrizA[j][i]
        matrizA[j][i] = matrizB[i][j]
        matrizB[i][j] = temp
    
print("Matrizes invertidas:")
for i in range(size):
    
    for j in range(size):
        
        print(end=f"{matrizA[i][j]} ")
    
    print()

print()

for i in range(size):
    
    for j in range(size):
        
        print(end=f"{matrizA[i][j]} ")
    
    print()