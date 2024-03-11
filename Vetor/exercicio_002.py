"2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."

vetor = []

print("Informe 10 numeros reais:")

for i in range(0, 10):

    num = int(input(f"Informe o numero {i + 1}: "))
    vetor.append(num)

print(end="Numeros inseridos na ordem inversa: ")

for i in range(9, -1, -1):

    print(end=f"{vetor[i] }  ")