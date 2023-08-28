#5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

import math

populacao_A = 0
populacao_B = 0
taxa_cresc_A = 0
taxa_cresc_B = 0
ano = 0
temp = 0
temp2 = 0

print("Informe a populão A: ")
populacao_A = float(input())
print("Informe a taxa de crescimento da populão A: ")
taxa_cresc_A = float(input())

print("Informe a populão B: ")
populacao_B = float(input())
print("Informe a taxa de crescimento da populão B: ")
taxa_cresc_B = float(input())

taxa_cresc_A = taxa_cresc_A/100
taxa_cresc_B = taxa_cresc_B/100

if populacao_A > populacao_B:

    temp = populacao_A
    populacao_A = populacao_B
    populacao_B = temp

    temp2 = taxa_cresc_A
    taxa_cresc_A = taxa_cresc_B
    taxa_cresc_B = temp2

while populacao_A < populacao_B:

    ano += 1
    populacao_A = populacao_A*math.pow(1 + taxa_cresc_A, ano)
    populacao_B = populacao_B*math.pow(1 + taxa_cresc_B, ano)

print("Anos necessários: {}".format(ano)) 




