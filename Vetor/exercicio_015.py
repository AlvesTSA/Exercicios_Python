"/*15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:"

#a. Mostre a quantidade de valores que foram lidos; 

#b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro; 

#c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;

#d. Calcule e mostre a soma dos valores;
 
#e. Calcule e mostre a média dos valores;

#f. Calcule e mostre a quantidade de valores acima da média calculada;

#g. Calcule e mostre a quantidade de valores abaixo de sete;

#h. Encerre o programa com uma mensagem; 

notas = []
count1 = 0

print("Informe as notas e digite -1 para finalizar:")

for i in range(0, 100):
    
    nota = float(input(f"Informe a nota {i + 1}: "))
    notas.append(nota)

    if notas[i] == -1:
        break
    
    count1 += 1


#//a. Mostre a quantidade de valores que foram lidos

print(f"Quantidade de valores lidos: {count1}")

#//b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print(end="Valores lidos: ")
for i in range(0, count1):
    
    print(end=f"{notas[i]} ")


#//c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
print("\nValores lidos na ordem inversa: ")
for i in range(count1 - 1, 0, -1):
    
    print(f"{notas[i]} ")


#//d. Calcule e mostre a soma dos valores;
soma = 0
for i in range(0, count1):
    
    soma += notas[i]

print(f"Soma: {soma}")

#//e. Calcule e mostre a média dos valores;
media = soma / count1
print(f"Media: {media}")

#//f. Calcule e mostre a quantidade de valores acima da média calculada;
count2 = 0
for i in range(0, count1):
    
    if (notas[i] > media):
        count2 += 1
    

print(f"Quantidade de valores acima da media: {count2}")

#//g. Calcule e mostre a quantidade de valores abaixo de sete;
count3 = 0
for i in range(0, count1):
    
    if (notas[i] < 7.0):
        count3 += 1
    

print(f"Quantidade de valores abaixo de 7: {count3}")

#//h. Encerre o programa com uma mensagem;

print("Obrigado pela participacao")