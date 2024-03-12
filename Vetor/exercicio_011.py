"/*11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.*/"

vetor10a = []
vetor10b = []
vetor10c = []
vetor30a = []

print("Informe os elementos do vetor A: ")

for i in range(0, 10):

    a = int(input())
    vetor10a.append(a)

print("Informe os elementos do vetor B: ")

for i in range(0, 10):

    b = int(input())
    vetor10b.append(b)

print("Informe os elementos do vetor C: ")

for i in range(0, 10):

    c = int(input())
    vetor10c.append(c)
    
for i in range(0, 10):

    vetor30a.append(vetor10a[i])
    vetor30a.append(vetor10b[i])
    vetor30a.append(vetor10c[i])

print("Elementos intercalados: ")

for i in range(0, 30):

    print(end=f"{vetor30a[i]} ")