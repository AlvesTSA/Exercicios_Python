"3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela."

vetor_nota = []
media = 0
print("Informe as 4 notas:")

for i in range(0, 4):

    nota = float(input(f"Informa a nota {i + 1}: "))
    vetor_nota.append(nota)

    media = vetor_nota[i] + media

media = media / 4
print("Notas:")

for i in range(0, 4):

    print(f"{vetor_nota[i]}")

print(f"Media: {media}")