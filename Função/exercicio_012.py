"""/*12. Faça uma função que leia um número não determinado de valores positivos e retorna a média aritmética dos mesmos.*/
"""

def mediaAritmetica():

    media = 0
    count = 0

    print("Informe numeros inteiros ou informe -1 para sair:")

    while True:
        numero = float(input())

        if (numero == -1):
            break
        
        media += numero
        count += 1
        
    if (count == 0): 
    
        return 0 # Evita divisão por zero se nenhum número for inserido
    
    return media / count 

media = mediaAritmetica()
print(f"Media aritmetica: {media:.2f}")