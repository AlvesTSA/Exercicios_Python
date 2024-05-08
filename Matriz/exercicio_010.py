"""/*10. Leia uma matriz 50 x 2, onde cada coluna corresponde a um lado de um triangulo retângulo. Declare um vetor que contenha a área dos respectivos triângulos e o escreva.*/"""

import random

size_l = 50
size_c  = 2
max = 10
min = 1
matriz = [[0 for _ in range(size_c)] for _ in range(size_l)]
vetor = [0 for _ in range(size_l)]
C = 0.5

print(f"Informe uma matriz {size_l} x {size_c}: ")
print()

for i in range(size_l):
    
    for j in range(size_c):
        
        matriz[i][j] = random.randint(min,max)
    
print("Matriz lida:")

for i in range(size_l):
    
    for j in range(size_c):
        
        print(end=f"{matriz[i][j]} ")
    
    print()

print("Areas dos triangulos: \n")

for i in range(size_l):
    
    vetor[i] = matriz[i][0] * matriz[i][1] * C
    print(end=f"{vetor[i]} ")