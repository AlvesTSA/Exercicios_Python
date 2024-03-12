"/*6. Leia um vetor de 20 posições e atribua valor 0 para todos os elementos que possuírem valores negativos.*/"

vetor = []

print("Informe 20 números inteiros:")

for i in range(0, 20):

    num = int(input())
    vetor.append(num)

    if(vetor[i] < 0):

        vetor[i] = 0

print("Valores lidos e corrigidos com 0:")

for num in vetor:

    print(end=f"{num} ")