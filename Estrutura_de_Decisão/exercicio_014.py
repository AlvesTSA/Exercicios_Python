#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
 
#Média de aproveitamento: entre 9.0 e 10.0; Conceito: A 
 
#Média de aproveitamento: entre 7.5 e 9.0; Conceito: B 

#Média de aproveitamento: entre 6.0 e 7.5; Conceito: C 
 
#Média de aproveitamento: entre 4.0 e 6.0; Conceito: D  

#Média de aproveitamento: entre 4.0 e 0.0; Conceito: E 

#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = 0
nota2 = 0
media = 0

print("Informe suas duas notas: ")
nota1 = float(input())
nota2 = float(input())

media = (nota1 + nota2)/2

if (media >= 9 and media <= 10):

    print("Nota 1: {}\nNota 2: {}\nMédia:  {}\nConceito: A\nSituação: APROVADO".format(nota1, nota2, media))
    
elif (media >= 7.5 and media < 9):

    print("Nota 1: {}\nNota 2: {}\nMédia:  {}\nConceito: B\nSituação: APROVADO".format(nota1, nota2, media))
    
elif (media >= 6 and media < 7.5):

    print("Nota 1: {}\nNota 2: {}\nMédia:  {}\nConceito: C\nSituação: APROVADO".format(nota1, nota2, media))
    
elif (media >= 4 and media < 6):

   print("Nota 1: {}\nNota 2: {}\nMédia:  {}\nConceito: D\nSituação: REPROVADO".format(nota1, nota2, media))
    
elif (media >= 0 and media < 4):
    
    print("Nota 1: {}\nNota 2: {}\nMédia:  {}\nConceito: E\nSituação: REPROVADO".format(nota1, nota2, media))

else:

    print("Informe um valor válido !")