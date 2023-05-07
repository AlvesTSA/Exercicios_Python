  #  Faça um programa para a leitura de duas notas parciais de um aluno. O    vprograma deve calcular a média alcançada por aluno e apresentar:

 # A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; 

# A mensagem "Reprovado", se a média for menor do que sete; 

# A mensagem "Aprovado com Distinção", se a média for igual a dez.


nota1 = 0
nota2 = 0
media = 0

print("Informe suas duas notas: ")
nota1 = float(input())
nota2 = float(input())

media = (nota1 + nota2)/2

if media >= 0 and media < 7 :

    print("REPROVADO")

elif media >= 7 and media < 10 :

    print("APROVADO")

elif media == 10 :

    print("APROVADO COM DISTINÇÃO")

else :

    print("NOTA INVÁLIDA")


    
