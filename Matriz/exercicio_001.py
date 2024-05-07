"""1. Leia uma matriz 3 x 3 e escreva a localização (linha e a coluna) do maior valor."""

size = 3 
matriz = []

for i in range(size):
    
    l = []

    for j in range(size):

        l.append(0)
    
    matriz.append(l)
    
print(f"Informe uma matriz {size} x {size}:")

for i in range(size):

    for j in range(size):

        matriz[i][j] = int(input())

maior = 0
linha = 0
coluna = 0

for i in range(size):

    for j in range(size):

        if matriz[i][j] > maior:

            maior = matriz[i][j]
            linha = i + 1
            coluna = j + 1

print(f"Maior valor: {maior}\nlocalização.\nlinha: {linha}\ncoluna: {coluna}")
