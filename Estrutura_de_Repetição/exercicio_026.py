#26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

eleitor = int(input("Informe a quantidade de eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range(1, eleitor+1):

    while True:

        candidato = int(input("Informe em qual candidato deseja votar [1] [2] [3]: "))

        match candidato:

            case 1:
                candidato1 += 1

            case 2:
                candidato2 += 1

            case 3:
                candidato3 += 1

            case _:
                print("Erro: informe 1, 2, ou 3")

        if candidato > 3:
            print("Tente novamente.")
        else:
            break

print("Candidato 1: {} votos".format(candidato1))
print("Candidato 2: {} votos".format(candidato2))
print("Candidato 3: {} votos".format(candidato3))