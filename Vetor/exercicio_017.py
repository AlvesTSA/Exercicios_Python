"/*17. Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:"

#Atleta: Rodrigo Curvêllo
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m


#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m*/

saltos = []
    
while True:
    
    print(end=f"\nAtleta: ")
    nome = input()

    if nome == "sair":
        break
    

    print(end="Primeiro salto: ")
    salto = float(input())
    saltos.append(salto) 
    print(end="Segundo salto: ")
    salto = float(input())
    saltos.append(salto)
    print(end="Terceiro salto: ")
    salto = float(input())
    saltos.append(salto)
    print(end="Quarto salto: ")
    salto = float(input())
    saltos.append(salto)
    print(end="Quinto salto: ")
    salto = float(input())
    saltos.append(salto)

    media = 0

    for y in range(0, 5):
        
        media += saltos[y]
    

    media /= 5

    print("\n\nResultado final\n")
    print(f"Atleta: {nome}")
    print(f"Saltos: {saltos[0]} - {saltos[1]} - {saltos[2]} - {saltos[3]} - {saltos[4]}")
    print(f"Media dos saltos: {media}\n\n")