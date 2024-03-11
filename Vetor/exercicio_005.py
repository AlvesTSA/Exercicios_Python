"5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores."

vetor = []
vetor_par = []
vetor_impar = []

print("Informe 20 numeros inteiros:")

for i in range(0, 20):

    num = int(input())
    vetor.append(num)

    resto = 0
    resto = vetor[i] % 2

    if (resto == 0):

        num_par = vetor[i]
        vetor_par.append(num_par)
       
    else:
        num_impar = vetor[i]
        vetor_impar.append(num_impar)
        
print("Valores inseridos:")

for i in range(0, 20):

    print(end=f"{vetor[i]} ")

print("\nValores impares:")

for num_impar in vetor_impar:

    print(end=f"{num_impar} ")

print("\nValores pares:")

for num_par in vetor_par:

    print(end=f"{num_par} ")