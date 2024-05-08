"""/*3. Leia uma matriz 20 x 20. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final escrever a localização (linha e coluna) ou uma mensagem de “não encontrado”. */"""

import random

size = 20
intervalo_max = 1000
intervalo_min = 0
matriz = []
loc = [[0],[0]]
count = 0
x = 0

for i in range(size):
    l = []
    for j in range(size):
        l.append(0)
    
    matriz.append(l)

x = int(input("Informe um valor de x: "))

for i in range(size):
    
    for j in range(size):
        
        matriz[i][j] = random.randint(intervalo_min,intervalo_max) 
    

for i in range(size):
    
    for j in range(size):
    
        if matriz[i][j] == x:
            
            loc[0] = i
            loc[1] = j

            print(f"Valor encontrado\nlinha: {loc[0]}\nColuna: {loc[1]}")
            count += 1
         
if count == 0:
    
    print("Valor nao encontrado")

