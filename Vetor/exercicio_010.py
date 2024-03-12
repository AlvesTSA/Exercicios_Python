"/*10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.*/"

vetor10a = []
vetor10b = []
vetor20a = []

print("Informe os elementos do vetor A: ")

for i in range(0, 10):

    a = int(input())
    vetor10a.append(a)

print("Informe os elementos do vetor B: ")

for i in range(0, 10):

    b = int(input())
    vetor10b.append(b)
    
for i in range(0, 10):

    vetor20a.append(vetor10a[i])
    vetor20a.append(vetor10b[i])

print("Elementos intercalados: ")

for i in range(0, 20):

    print(end=f"{vetor20a[i]} ")