#/*Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 2 situações:
#a)comprar apenas latas de 18 litros;
#b)comprar apenas galões de 3,6 litros;

area = 0
lata = 0
galao = 0
litros_necessario = 0
valor_galao = 0
valor_lata = 0

print("Informe a área a ser pintada: ")
area = float(input())

litros_necessario = area/6
lata = litros_necessario/18
galao = litros_necessario/3.6
valor_galao = galao*25
valor_lata = lata*80

print("Quantidade de galões: {}".format(galao))
print("Valor em galões R$: {}".format(valor_galao))
print("Quantidade de latas: {}".format(lata))
print("Valor em latas R$: {}".format(valor_lata))


