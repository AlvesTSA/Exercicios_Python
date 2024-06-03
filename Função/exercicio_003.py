"""/*3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.*/
"""

def sum( a, b, c):

    resultado = a + b + c

    return resultado

num = [0,0,0]

for i in range(0,3):
    print(f"Informe o número {i + 1}: ")
    num[i] = float(input())

result = sum(num[0],num[1],num[2])
print(f"Soma dos números: {result}")
