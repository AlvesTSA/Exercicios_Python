"""/*6. Declare uma matriz 5 x 5. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida.*/"""

size = 5
matriz = [[0 for _ in range(size)] for _ in range(size)]

for i in range(size):

    for y in range(size):
        
        if(i == y):

            matriz[i][y] = 1
        
        else:

            matriz[i][y] = 0
        
print("Matriz resultante:")

for i in range(size):
    
    for y in range(size):
        
        print(end=f"{matriz[i][y]} ")
    
    print()