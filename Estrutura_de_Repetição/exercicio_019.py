#19. . Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = 0
num = 0
menor = 0
maior = 0
soma = 0

print(end="Informe quantos numeros deseja incluir: ")
n = int(input())
print("Informe os números entre 0 e 1000:")

while True:

    num = int(input())

    if num <= 0 or num >= 1000:
        print("Erro: informe numeros entre 0 e 1000")
    else:
        break

maior = num
menor = num
soma = num

for i in range(1, n):

    while True:

        num = int(input())

        if num <= 0 or num >= 1000:
            print("Erro: informe numeros entre 0 e 1000")
        else:
            break

    soma += num

    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print("Maior: {}\nMenor: {}\nSoma: {}".format(maior, menor, soma))