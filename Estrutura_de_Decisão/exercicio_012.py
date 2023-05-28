#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do imposto de Renda, INSS, Sindicato e que o FGTS corresponde a 11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
 
#Desconto do IR; 

#Salário Bruto ate R$900,00 (inclusive) – Isento; 

#Salário Bruto de R$ 1500, 00 (inclusive) – desconto de 5%;

#Salario bruto até R$ 2500,00 (Inclusive) – desconto de 10%;
  
#Salário bruto acima de 2500 – Desconto de 20%.

#Imprima na tela as informações dispostas conforme o exemplo abaixo.
  
#Salário bruto: R$ 

#Desconto IR: R$ 
 
#Desconto INSS (10%): R$
 
#Desconto Sindicato (3%): R$  
 
#FGTS (11%) 
  
#Desconto total: R$ 
  
#Salário líquido: R$

ganho_hora = 0
hora_mes = 0
salario_bruto = 0
salario_liquido = 0
desconto_IR = 0
desconto_INSS = 0
desconto_Sind = 0
fgts = 0
desconto_total = 0

print("Informe quanto você ganha por hora: ")
ganho_hora = float(input())
print("Informe quantas horas trabalhou no mês: ")
hora_mes = float(input())

salario_bruto = ganho_hora*hora_mes

if (salario_bruto <= 900 and salario_bruto > 0):

    desconto_INSS = salario_bruto*0.1
    desconto_Sind = salario_bruto*0.03
    desconto_total = desconto_IR + desconto_INSS + desconto_Sind
    salario_liquido = salario_bruto - desconto_total
    fgts = salario_bruto*0.11

    print("Salário bruto: R$ {}\nDesconto IR (0 porcento): R$ {}\nDesconto INSS (10 porcento): R$ {}\nDesconto Sindicato (3 porcento): R$ {}\nFGTS (11 porcento): R$ {}\nDesconto total: R$ {}\nSalário líquido: R$ {}".format(salario_bruto, desconto_IR, desconto_INSS, desconto_Sind, fgts, desconto_total, salario_liquido))

elif (salario_bruto > 900 and salario_bruto <= 1500):

    desconto_IR = salario_bruto*0.05
    desconto_INSS = salario_bruto*0.1
    desconto_Sind = salario_bruto*0.03
    desconto_total = desconto_IR + desconto_INSS + desconto_Sind
    salario_liquido = salario_bruto - desconto_total
    fgts = salario_bruto*0.11

    print("Salário bruto: R$ {}\nDesconto IR (5 porcento): R$ {}\nDesconto INSS (10 porcento): R$ {}\nDesconto Sindicato (3 porcento): R$ {}\nFGTS (11 porcento): R$ {}\nDesconto total: R$ {}\nSalário líquido: R$ {}".format(salario_bruto, desconto_IR, desconto_INSS, desconto_Sind, fgts, desconto_total, salario_liquido))

elif (salario_bruto > 1500 and salario_bruto <= 2500):

    desconto_IR = salario_bruto*0.1

    desconto_INSS = salario_bruto*0.1
    desconto_Sind = salario_bruto*0.03
    desconto_total = desconto_IR + desconto_INSS + desconto_Sind
    salario_liquido = salario_bruto - desconto_total
    fgts = salario_bruto*0.11

    print("Salário bruto: R$ {}\nDesconto IR (10 porcento): R$ {}\nDesconto INSS (10 porcento): R$ {}\nDesconto Sindicato (3 porcento): R$ {}\nFGTS (11 porcento): R$ {}\nDesconto total: R$ {}\nSalário líquido: R$ {}".format(salario_bruto, desconto_IR, desconto_INSS, desconto_Sind, fgts, desconto_total, salario_liquido))

elif (salario_bruto > 2500):

    desconto_IR = salario_bruto*0.2
    desconto_INSS = salario_bruto*0.1
    desconto_Sind = salario_bruto*0.03
    desconto_total = desconto_IR + desconto_INSS + desconto_Sind
    salario_liquido = salario_bruto - desconto_total
    fgts = salario_bruto*0.11

    print("Salário bruto: R$ {}\nDesconto IR (20 porcento): R$ {}\nDesconto INSS (10 porcento): R$ {}\nDesconto Sindicato (3 porcento): R$ {}\nFGTS (11 porcento): R$ {}\nDesconto total: R$ {}\nSalário líquido: R$ {}".format(salario_bruto, desconto_IR, desconto_INSS, desconto_Sind, fgts, desconto_total, salario_liquido))

else:

    print("Informe um valor válido !")