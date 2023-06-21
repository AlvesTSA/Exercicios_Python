#Um posto está vendendo combustíveis com a seguinte tabela de descontos

# Álcool:
 
# Até 20 litros: desconto de 3% por litro;
# Acima de 20 litros: Desconto de 5% por litro.

# Gasolina:

# Até 20 litros: desconto de 4% por litro
# Acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool. G-gasolina), calcule e imprima o valor a ser pago pelo cliente.*/

import sys

op = ""
litro = 0
preco_litro = 0
desconto = 0
valor = 0

print("Informe quantos litros deseja: ")
litro = float(input())
print("Informe o tipo de combustível\nA-álcool\nG-gasolina")
op = input()

match op:

    case 'A':

        if(litro > 0 and litro <= 20):

            preco_litro = 4
            desconto = preco_litro*0.03
            preco_litro = preco_litro - desconto
            valor = litro*preco_litro
        else:

            preco_litro = 4
            desconto = preco_litro*0.05
            preco_litro = preco_litro - desconto
            valor = litro*preco_litro

    case 'G':

        if(litro > 0 and litro <= 20):

            preco_litro = 5
            desconto = preco_litro*0.04
            preco_litro = preco_litro - desconto
            valor = litro*preco_litro
        else:

            preco_litro = 5
            desconto = preco_litro*0.06
            preco_litro = preco_litro - desconto
            valor = litro*preco_litro

    case _:

        print("VALOR INVÁLIDO !")

        sys.exit(0)

print("VAlor a pagar R$: {:.2f}".format(valor))