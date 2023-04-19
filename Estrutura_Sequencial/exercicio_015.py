#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#a)salário bruto.
#b)quanto pagou ao INSS.
#c)quanto pagou ao sindicato.
#d)quanto pagou de IR.
#e)desconto total.
#f)o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

salario_bruto = 0
salario_liquido = 0
desconto_inss = 0
desconto_ir = 0
desconto_sin = 0
desconto_total = 0
ganho_hora = 0
hora_mes = 0

print("Quanto você ganha por hora: ")
ganho_hora = float(input())

print("Quantas horas trabalhou no mes: ")
hora_mes = float(input())

salario_bruto = ganho_hora*hora_mes
desconto_inss = salario_bruto*0.08
desconto_sin = salario_bruto*0.05
desconto_ir = salario_bruto*0.11
desconto_total = desconto_inss + desconto_sin + desconto_ir
salario_liquido = salario_bruto - desconto_total

print("Salário bruto R$: {}".format(salario_bruto))
print("Desconto INSS R$: {}".format(desconto_inss))
print("Desconto sindicato R$: {}".format(desconto_sin))
print("Desconto IR R$: {}".format(desconto_ir))
print("Desconto total R$: {}".format(desconto_total))
print("Sálario líquido R$: {}".format(salario_liquido))


