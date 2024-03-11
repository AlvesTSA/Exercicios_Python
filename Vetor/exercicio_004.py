"4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes."

vetor = []
count = 0

print("Informe 10 caracteres de letras:")

for i in range(0, 10):

    caractere = input(f"Informe o caractere {i + 1}: ")
    vetor.append(caractere)

    if (vetor[i] != 'a' and vetor[i] != 'e' and vetor[i] != 'i' and vetor[i] != 'o' and vetor[i] != 'u' and vetor[i] != 'A' and vetor[i] != 'E' and vetor[i] != 'I' and vetor[i] != 'O' and vetor[i] != 'U'):

        count = count + 1

print(f"Foram lidas: {count} consoantes")
print("Consoantes lidas:")

for i in range(0, 10):

    if (vetor[i] != 'a' and vetor[i] != 'e' and vetor[i] != 'i' and vetor[i] != 'o' and vetor[i] != 'u' and vetor[i] != 'A' and vetor[i] != 'E' and vetor[i] != 'I' and vetor[i] != 'O' and vetor[i] != 'U'):

        print(f"{vetor[i]} ")