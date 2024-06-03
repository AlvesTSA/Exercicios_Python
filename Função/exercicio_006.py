"""/*6. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.*/
"""

def transformaIdade(anos,meses,dias):
    return anos * 365 + meses * 30 + dias

anos = int(input("Informe os anos de sua idade: "))
meses = int(input("Informe os meses de sua idade: "))
dias = int(input("Informe os dias de sua idade: "))

d = transformaIdade(anos,meses,dias)

print(f"Voce tem {d} dias de idade.")