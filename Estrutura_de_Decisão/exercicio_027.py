# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
 
# Até 5 Kg de File Duplo: R$ 4,90 por Kg 
# Acima de 5 Kg de File Duplo: R$ 5,80 por Kg
 
# Até 5 Kg de Alcatra: R$  5,90 por Kg 
# Acima de 5 Kg de Alcatra: R$ 6,80 por Kg

# Até 5 Kg de Picanha: R$  6,90 por Kg 
# Acima de 5 Kg de Picanha: R$ 7,80 por Kg

# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

import sys

op = 0
op2 = 0
kilo = 0
valor = 0
desconto = 0
valor_pago = 0
tipo_carne = ""
tipo_pag = ""

print("nforme a quantidade de carne: ")
kilo = float(input())
print("Informe o tipo de carne\n[1]-Filé Duplo\n[2]-Alcatra\n[3]-Picanha")
op = int(input())

match op:
    case 1: 
        tipo_carne = "File Duplo"

        if(kilo > 0 and kilo <= 5):

            valor = kilo*4.90

        else:

            valor = kilo*4.80

    case 2: 
        tipo_carne = "Alcatra"

        if(kilo > 0 and kilo <= 5):

            valor = kilo*5.90

        else:

            valor = kilo*6.80

    case 3: 
        tipo_carne = "Picanha"

        if(kilo > 0 and kilo <= 5):

            valor = kilo*6.90

        else:

            valor = kilo*7.80
    case _:

        print("VALOR INVÁLIDO !")

        sys.exit(0)

print("Informe a forma de pagamento\n[1]-Cartão tabajara\n[2]-Outro cartão")
op2 = int(input())

match op2:

    case 1:
        tipo_pag = "Cartão Tabajara"

        desconto = valor*0.05
        valor_pago = valor - desconto

    case 2:
        tipo_pag = "Outro Cartão"

        valor_pago = valor
    
    case _:

        print("VALOR INVÁLIDO !")

        sys.exit(0)

print("\nInformações da compra\nTipo de carne: {}\nPeso: {:.2f}\nPreço total: {:.2f}\nTipo de pagamento: {}\nValor do desconto: {:.2f}\nValor a pagar: {:.2f}".format(tipo_carne,kilo,valor,tipo_pag,desconto,valor_pago,))


