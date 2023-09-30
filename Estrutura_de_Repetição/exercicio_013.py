#13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

base = 0
expoente = 0
resultado = 0

print("Informe a base:")
base = int(input())
print("Informe o expoente:")
expoente = int(input())
resultado = base
contador = 0

print(end="{} elevado a {} = ".format(base, expoente))

if expoente > 0:

    while contador < expoente - 1:
        
        contador += 1
        resultado *= base

elif expoente < 0:

    expoente *= -1

    while contador < expoente - 1:
        
        contador += 1
        resultado *= base
    
    resultado = 1 / resultado

else: 
    resultado = 1

print("{}".format(resultado))