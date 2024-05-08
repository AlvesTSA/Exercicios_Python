"""/*9. Leia uma matriz 6 x 6 e atribuir o valor 0 para os valores negativos encontrados fora das diagonais principal e secundaria.*/
"""

import random

size = 6
max = 10
min = 0
matriz = [[0 for _ in range(size)] for _ in range(size)]

print(f"Informe uma matriz {size} x {size}: ")

for i in range(size):
    
    for j in range(size):
        
        num = random.randint(min,max)
        matriz[i][j] = num * -1
    
for i in range(size):
    
    for j in range(size):
        
        if (i != j and j != size - i - 1 and matriz[i][j] < 0):
            
            matriz[i][j] = 0
        
for i in range(size):
    
    for j in range(size):
        
        print(end=f"{matriz[i][j]} ")
    
    print()
