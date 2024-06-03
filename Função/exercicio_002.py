"""/*2. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.*/
"""

def somaImposto(taxaImposto, custo):

    return custo + (custo*(taxaImposto / 100))

taxaImposto = float(input("Informe o a taxa de imposto: "))
custo = float(input("Informe o custo do preoduto: "))
custo_final = somaImposto(taxaImposto,custo)

print("Valor do produto com imposto: {:.2f}".format(custo_final))