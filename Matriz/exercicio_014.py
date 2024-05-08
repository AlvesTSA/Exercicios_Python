"""/*14. Faça um jogo de batalha naval, utilize as seguinte regras:

– O primeiro usuário será o que vai configurar o tabuleiro inserindo os navios.
– O tabuleiro deve ter 8×8
– Quando inserido todos os navios o restante será considerado como “água”.
– Cada navio pode ocupar apenas 1 posição
– O jogador deve respeitar o espaço de 1 célula entre os navios
– O jogador que irá descobrir onde os navios estão tem apenas 10 tiros
– O jogador 1 pode posicionar 5 navios */"""

import random

size = 8
tabuleiro = [[0 for _ in range(size)] for _ in range(size)]
linha = 0
coluna = 0
tiros = 10
quant_navios = 5

for i in range(quant_navios):

    while True:
        linha = random.randint(1,size) - 1
        coluna = random.randint(1,size) - 1

        if (tabuleiro[linha][coluna] == 1):
            continue
        else:
            break
    
    tabuleiro[linha][coluna] = 1

abatido = 0

for i in range(tiros):
    
    linha = int(input("infome linha: "))
    coluna = int(input("infome coluna: "))
    linha -= 1 
    coluna -= 1

    if (tabuleiro[linha][coluna] == 1):
        
        print("Navio abatido.")
        abatido+=1
    
    else:

        print("Errou")
    
print(f"Voce afundou {abatido} navio(s)")