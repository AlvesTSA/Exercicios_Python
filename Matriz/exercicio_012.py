"""/*12. Leia uma matriz 4 x 4 e verifique se é palíndromo, isto é, sua leitura a partir de qualquer direção sempre apresentara a mesma seqüência.EX.                 SATOR
                    AREPO
                    TENET
                    OPERA
                    ROTAS
                        */"""

size = 4
matriz = [[' ' for _ in range(size)] for _ in range(size)]
polindromo = False

print(f"Informe uma matriz tipo char {size} x {size}: ")

for i in range(size):

    for j in range(size):
    
        matriz[i][j] = input()

for i in range(size):

    for j in range(size):
    
        if (matriz[i][j] != matriz[(size-1) - i][(size - 1) - j]):
            
            polindromo = False

            break

if (polindromo):

    print("Matriz:")

    for i in range(size):

        for j in range(size):
            
            print(end=f"{matriz[i][j]} ")
        
        print()
    
    print("A matriz e um polindromo")

else:

    print("Matriz:")

    for i in range(size):

        for j in range(size):
        
            print(end=f"{matriz[i][j]} ")

        print()

    print("A matriz nao e polidromo")