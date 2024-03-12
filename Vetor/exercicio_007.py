"/*7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.*/"

vetor = []
soma = 0
produto = 1

print("Informe 5 números inteiros:")

for i in range(0, 5):

    num = int(input(f"Informe o {i + 1}: "))
    vetor.append(num)

    soma = soma + vetor[i]
    produto = produto * vetor[i]

print(f"Soma: {soma}")
print(f"Multiplicação: {produto}")
print(end="Valores lidos:")

for num in vetor:

    print(end=f"{num} ")