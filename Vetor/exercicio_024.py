"/*24. Leia um vetor de 5 posições contendo os caracteres de um numero. Em seguida escreva esse numero por extenso.*/"

vetor = [0,0,0,0,0]

for i in range(0, 5):
    
    vetor[i] = int(input(f"Informe o carctere {i + 1}: "))

print(end="Numero: ")

for i in range(0, 5):
    
    print(end=f"{vetor[i]}")
