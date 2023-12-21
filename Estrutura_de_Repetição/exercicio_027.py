#27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

n = int(input("Informe quantas turmas deseja incluir: "))
soma = 0

for i in range(1, n+1):

    while True:
        alunos = float(input("Informe a quantidade de alunos da turma {}: ".format(i)))

        soma += alunos

        if alunos > 40:
            print("Erro: a turma deve ter no máximo 40 alunos.")
        else:
            break

media = soma / n

print("Número médio de alunos por turma: {}".format(media))