"""/*13.Crie um tabuleiro de jogo da velha, usando uma matrizes de caracteres (char) 3×3, onde o usuário pede o número da linha (1 até 3) e o da coluna (1 até 3). A cada vez que o usuário entrar com esses dados, colocar um ‘X’ ou ‘O’ no local selecionado.*/"""

size = 3
matriz = [[' ' for _ in range(size)] for _ in range(size)]
i = 0
j = 0

for z in range(size*size):

    while True:
        
        i = int(input("Informe a linha: "))
        j = int(input("Informe a coluna: "))

        if ((i < 1 or i > size) or (j < 1 or j > size)):
            
            print(f"ERRO: Valor invalido, informe de 1 a {size}")

        elif (matriz[i-1][j-1] == 'X' or matriz[i-1][j-1] == 'O'):
        
            print("ERRO: Esse espaco ja foi preenchido.")
            
        else:
            break

    if (z % 2 == 0):

        matriz[i-1][j-1] = 'X'
    
    else:

        matriz[i-1][j-1] = 'O'
    
print("Resultado do jogo:")
for w in range(size):
    
    for z in range(size):
        
        print(end=f"{matriz[w][z]} ")
    
    print()