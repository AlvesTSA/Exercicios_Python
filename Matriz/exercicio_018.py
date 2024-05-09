"""/*18. Leia uma matriz 5 x 5 e faça uma troca entre as diagonais superior e inferior. Escreva-a ao final.*/"""

import random

size = 5
max = 10
min = 0
matriz = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):

    for j in range(size):
        
        matriz[i][j] = random.randint(min,max)
    
print("Matriz original:")
for i in range(size):
    
    for j in range(size):
        
        print(end=f"{matriz[i][j]} ")
    
    print()

print()
temp = 0

for i in range(size):
    
    for j in range((i + 1),size):
        
        temp = matriz[i][j]
        matriz[i][j] = matriz[j][i]
        matriz[j][i] = temp
    
print("Matriz invertida:")
for i in range(size):
    
    for j in range(size):
        
        print(end=f"{matriz[i][j]} ")
    
    print()