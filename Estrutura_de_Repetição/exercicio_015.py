#15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

n = 0
num1 = 0
num2 = 1
num3 = 0

print("Informe até qual termo deseja calcular: ")
n = int(input())

for i in range(1, n + 1):

    num3 = num1 + num2
    num1 = num2
    num2 = num3

    print(end="{} ".format(num1))