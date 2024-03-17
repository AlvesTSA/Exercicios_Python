"/*23. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.*/"

import random

contador = [0,0,0,0,0,0]

for i in range(0, 100):

    numero = random.randint(1, 6)
    contador[numero - 1] += 1

for i in range(0, 6):

    print(f"Numero {i + 1}: {contador[i]} vezes") 

