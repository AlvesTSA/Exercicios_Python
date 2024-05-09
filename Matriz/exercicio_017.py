"""/*17. Leia uma matriz 8 x 8 e a transforme numa matriz triangular inferior , atribuindo zero a todos os elementos acima da diagonal principal, escrevendo-a ao final.*/"""

import random

size = 8
max = 10
min = 0
matriz = [[0 for _ in range(size)] for _ in range(size)]

for w in range(size):

    for z in range(size):
        
        matriz[w][z] = random.randint(min,max)
    
for i in range(size):
    
    for j in range(size):
        
        if (j > i):
            
            matriz[i][j] = 0
        
        print(end=f"{matriz[i][j]} ")
    
    print()  