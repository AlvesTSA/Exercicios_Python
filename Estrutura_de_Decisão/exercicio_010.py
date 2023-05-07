# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = 0

print("Qual turno você estuda ?\nInforme uma letra correspondente\n  M-matutino\n  V-Vespertino\n  N-Noturno")
turno = input()

match turno :

    case 'M' :
        print("BOM DIA !")

    case 'V' :
        print("BOA TARDE !")

    case 'N' :
        print("BOA NOITE !")

    case _ :
        print("VALOR INVÁLIDO !")


