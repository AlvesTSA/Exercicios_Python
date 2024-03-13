"/*14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:"

"Telefonou para a vítima?" 

"Esteve no local do crime?" 

"Mora perto da vítima?"

"Devia para a vítima?"

"Já trabalhou com a vítima?"

"O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como 'Suspeita', entre 3 e 4 como 'Cúmplice' e 5 como 'Assassino'. Caso contrário, ele será classificado como 'Inocente'.*/"

resposta = []
s = 0

print("Responda as perguntas com s para sim e n para nao\n")
print("Telefonou para a vítima?")
respost = input()
resposta.append(respost)
print("Esteve no local do crime?")
respost = input()
resposta.append(respost)
print("Mora perto da vítima?")
respost = input()
resposta.append(respost)
print("Devia para a vítima?")
respost = input()
resposta.append(respost)
print("Já trabalhou com a vítima?")
respost = input()
resposta.append(respost)

for i in range(0, 5):
        
    if resposta[i] == "s" or resposta[i] == "S": 
        
        s = s + 1
    
if s == 2:
        
    print("Suspeita")

elif s > 2 and s < 5:

    print("Cumplice")

elif s == 5:

    print("Assassino")

else:

    print("Inocente")