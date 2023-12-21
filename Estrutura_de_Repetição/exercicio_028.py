#28. Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

q_cd = int(input("Informe a quantidade de cd: "))
soma = 0

for i in range(1, q_cd+1):

    valor_cd = float(input("Informe o valor do cd {}: ".format(i)))

    soma += valor_cd

media = soma / q_cd

print("Valor total: {}".format(soma))
print("Valor medio: {}".format(media))