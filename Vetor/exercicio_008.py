"/*8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.*/"

idadeV = []
alturaV = []

for i in range(0, 5):

    idade = int(input(f"Informe a idade da pessoa {i + 1}: "))
    idadeV.append(idade)
    altura = float(input(f"Informe a altura da pessoa {i + 1}: "))
    alturaV.append(altura)

for i in range(4, -1, -1):

    print(f"Idade da pessoa {i + 1}: {idadeV[i]}")
    print(f"Altura da pessoa {i + 1}: {alturaV[i]}")