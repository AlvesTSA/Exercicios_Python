"""/*11. Leia uma matriz 100 x 10 que se refere respostas de 10 questões de múltipla escolha, referentes a 100 alunos. Leia também um vetor de 10 posições contendo o gabarito de respostas que podem ser a, b, c ou d. Seu programa deverá comparar as respostas de cada candidato com o gabarito e emitir um vetor Resultado, contendo a pontuação correspondente.*/"""

import random

size_l = 100
size_c = 10
respostas = ['a', 'b', 'c', 'd']
size = len(respostas)
matriz = [[' ' for _ in range(size_c)] for _ in range(size_l)]
gabarito = [' ' for _ in range(size_c)]
resultado = [0 for _ in range(size_l)]
count_acerto = [0 for _ in range(size_l)]

#Geração do gabarito
for i in range(size_c):

    gabarito[i] = respostas[random.randint(0,size - 1)]

for i in range(size_l):
    
    print(f"Respostas do Aluno {(i+1)}: ")

    for j in range(size_c):
        
        matriz[i][j] = respostas[random.randint(0,size - 1)]
        print(end=f"{matriz[i][j]} ")
    
    print()

for i in range(size_l):
    
    for j in range(size_c):
        
        if (matriz[i][j] == gabarito[j]):
            
            resultado[i] += 10
            count_acerto[i] += 1
        
        else:
            
            resultado[i] += 0

print("\nGabarito: ")

for i in range(size_c):
    
    print(end=f"{gabarito[i]} ")

print("\n")

for i in range(size_l):

    print(f"Resultado do aluno {(i+1)}: {count_acerto[i]} acertos e {resultado[i]} pontos.")  
