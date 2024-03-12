"/*12. Foram anotadas as idades e alturas de 10 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.*/"

idadev = []
alturav = []
media = 0

for i in range(0, 10):
    
    idade = int(input(f"Informe a idade do aluno {i + 1}: "))
    idadev.append(idade)
    altura = float(input(f"Informe a altura do aluno {i + 1}: "))
    alturav.append(altura)
    
    media = media + alturav[i]


media = media / 10
count = 0

for i in range(0, 10):
    
    if idadev[i] > 13 and alturav[i] < media: 
        
        count = count + 1
    

print(f"Alunos com mais de 13 anos com altura inferior a media: {count}")
