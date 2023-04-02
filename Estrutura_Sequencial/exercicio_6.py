#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('Entre com o valor do raio: '))

area = 3.14 * (raio * raio)

print("A área do círculo: {:.2f}".format(area))