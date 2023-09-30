#11. Altere o programa anterior para mostrar no final a soma dos números.

num1 = 0
num2 = 0
temp = 0
i = 0
soma = 0

print("Informe dois números:")
num1 = int(input())
num2 = int(input())

if num1 > num2:

    temp = num1
    num1 = num2
    num2 = temp
    
print("Intervalo entre {} e {}: ".format(num1, num2))

while num1 < num2 - 1:
     
    num1 += 1
    soma += num1
    print("{}".format(num1))
    
print("\nSoma: {}".format(soma))