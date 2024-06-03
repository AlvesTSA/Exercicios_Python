"""import tabuada/*15. Faça um procedimento que recebe, por parâmetro, um valor N e calcula e escreve a tabuada de 1 até N. Mostre a tabuada na forma:

1 x N = N
2 x N = 2N
...
N x N = N^2*/
"""

def tabuada(N):
    for i in range(1,N+1):
        print(f"{i} x {N} = {N*i}")

print(end="Informe o numero que deseja ver a tabuada: ")
N = int(input())

tabuada(N)