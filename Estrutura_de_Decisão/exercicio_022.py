#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

#“Telefonou para a vítima? “ 
#“Esteve no local do crime?” 
#“Mora perto da vítima? “
#“Devia para a vítima? “
#“Já trabalhou com a vítima? “

#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”, entre 3 e 4 como “Cúmplice” e 5 como “Assassino“. Caso contrário, ele será classificado como “Inocente“.

contador = 0
resposta1 = 0
resposta2 = 0
resposta3 = 0
resposta4 = 0
resposta5 = 0

print("Responda com 's' para sim e 'n' para não\nTelefonou para a vítima?")
resposta1 = input()
print("Esteve no local do crime?")
resposta2 = input()
print("Mora perto da vítima?")
resposta3 = input()
print("Devia para a vítima?")
resposta4 = input()
print("Já trabalhou com a vítima?")
resposta5 = input()

if(resposta1 == 's'):

    contador += 1

if(resposta2 == 's'):

   contador += 1

if(resposta3 == 's'):

    contador += 1

if(resposta4 == 's'):

    contador += 1

if(resposta5 == 's'):

    contador += 1

if(contador == 2):

    print("Suspeito")

elif(contador >= 3 and contador <= 4):

    print("Cumplice")

elif(contador == 5):

    print("Culpado")

else:

    print("Inocente")

