#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1- Domingo , 2- Segunda, etc). Se digitar outro valor, deve aparecer “valor inválido.

dia = 0

print("Informe um valor de 1 a 7: ")
dia = int(input())

match (dia):

    case 2:
        print("SEGUNDA")

    case 3:
        print("TERÇA FEIRA")
        
    case 4:
        print("QUARTA FEIRA")
        
    case 5:
        print("QUINTA FEIRA")
    
    case 6:
        print("SEXTA FEIRA")
    
    case 7:
        print("SABADO")
    
    case 1:
        print("DOMINGO")

    case _:
        print("VALOR INVÁLIDO")


