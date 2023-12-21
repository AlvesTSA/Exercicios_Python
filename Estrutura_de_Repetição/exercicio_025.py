#25. Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

n = int(input("Informe quantas pessoas deseja incluir a idade: "))
soma = 0

for i in range(1, n+1):

    idade = int(input("Informe a idade da pessoa {}: ".format(i)))

    soma += idade

media = soma / n

if media > 0 and media < 26:
    print("Turma jovem")

elif media >= 26 and media <= 60:
    print("Turma adulta")

else:
    print("Turma idosa")