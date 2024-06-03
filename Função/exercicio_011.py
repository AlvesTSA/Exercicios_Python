"""/*11. A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando dados sobre o salário e número de filhos. Faça um procedimento que leia esses dados para um número não determinado de pessoas e retorne a média de salário da população, a média do número de filhos, o maior salário e o percentual de pessoas com salário até R$350,00.*/
"""

def pesquisa():

    count = 0
    count2 = 0
    media_salario = 0.0
    media_filhos = 0.0
    maior_salario = 0.0

    print("Preencha os dados ou digite -1 nos dois campos para sair\n")
    
    while True:
    
        print(end="Informe seu salario: ")
        salario = float(input())
        print(end="Informe quantos filhos voce tem: ")
        num_filhos = float(input())

        if (salario == -1 and num_filhos == -1):
            break
        
        count2 += 1
        
        media_salario += salario
        media_filhos += num_filhos

        if (salario > maior_salario):
        
            maior_salario = salario
        
        if (salario > 0 and salario <= 350):
        
            count += 1
        
    if (count2 > 0): 
    
        media_salario /= count2
        media_filhos /= count2
    
    percentual = (count*100) / count2
    
    return media_salario, media_filhos, maior_salario, percentual

mediaPerc = pesquisa()
    
print(f"Media salarial: {mediaPerc[0]:.2f}")
print(f"Media de filhos: {mediaPerc[1]:.0f}")
print(f"Maior salario: {mediaPerc[2]:.2f}")
print(f"Percentual de salario ate R$ 350,00: {mediaPerc[3]:.2f}%")