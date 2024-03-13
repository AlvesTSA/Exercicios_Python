"/*13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).*/"

tempv = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "junho", "julho", "Agosto", "Setermbro", "Outubro", "Novembro", "Dezembro"]
media = 0

for i in range(0, 12):
        
    temp = float(input(f"Informe a temperatura media do mes de {meses[i]}: "))
    tempv.append(temp)
    media = media + tempv[i]

media = media / 12
print("Meses com temperatura acima da media anual\n")

for i in range(0, 12):
    
    if tempv[i] > media:
        
        print(f"{i + 1} - { meses[i]}: {tempv[i]} °C")