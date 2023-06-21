#Para doar sangue é necessário ter entre 18 e 67 anos. Faça um aplicativo que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não. Use alguns dos operadores lógicos OU (||) e E (&&).

idade = 0

print("Informe sua idade: ")
idade = int(input())

if(idade >= 18 and idade <= 67):

    print("Você é um doador")

else: 

    print("Você não é um doador")
