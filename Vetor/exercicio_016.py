"/*16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:"

 #a. $200 - $299 

 #b. $300 - $399 

 #c. $400 - $499

 #d. $500 - $599

 #e. $600 - $699
 
 #f. $700 - $799
 
 #g. $800 - $899

 #h. $900 - $999

 #i. $1000 em diante

#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.*/"

contador = [0,0,0,0,0,0,0,0,0]
taxa_comiss = 0.09

for i in range(0, 100):
    
    print(end=f"Informe a o valor de venda do vendedor {i + 1}: ")
    venda = float(input())

    if venda == -1:
        
        break
    

    salario = (venda*taxa_comiss) + 200
    salario /= 100

    if salario >= 10:

        contador[8] += 1
    
    else:
        faixa = int(salario) 
        contador[faixa - 2] += 1
    

print(f"a. $200 - $299: {contador[0]} vendedores")
print(f"b. $300 - $399: {contador[1]} vendedores")
print(f"c. $400 - $499: {contador[2]} vendedores")
print(f"d. $500 - $599: {contador[3]} vendedores")
print(f"e. $600 - $699: {contador[4]} vendedores")
print(f"f. $700 - $799: {contador[5]} vendedores")
print(f"g. $800 - $899: {contador[6]} vendedores")
print(f"h. $900 - $999: {contador[7]} vendedores")
print(f"i. $1000 em diante: {contador[8]} vendedores")