# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = 0

while True: #funciona como um do-while

    print("Informe uma nota entre zero e dez: ")
    nota = int(input())

    if nota > 0 and nota < 10:

        print("Nota atribuida com sucesso.")
        break
    else: 

        print("Nota inválida.")
