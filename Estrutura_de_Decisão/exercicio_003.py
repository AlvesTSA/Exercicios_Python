#  Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra = 0

print("Informe uma letra correspondente com o sexo\nF - Feminino\nM - Masculino ")
letra = input()

if letra == 'F' or letra == 'f':

    print("FEMININO")

elif letra == 'M' or letra == 'm' :

    print("MASCULINO")

else :

    print("SEXO INVÁLIDO")

    

