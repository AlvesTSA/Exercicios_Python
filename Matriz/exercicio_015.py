"""/*15. Crie uma agenda que armazena, código da pessoa, número do telefone, idade. Sua agenda deve possibilitar:

(1) – inserir um contato
(2) – Remover um contato
(3) – Editar um contato
(4) – buscar um contato pelo Código.*/"""

max_pessoas = 100
n_campo = 3
pessoas = [[' ' for _ in range(n_campo)] for _ in range(max_pessoas)]
op = 0
op_1 = 0
codigo = ' '
fim = 0
count_pessoas = 0

for w in range(max_pessoas):

    while True:
    
        print("Escolha uma opcao a seguir.\n\n(1)  inserir um contato\n(2)  Remover um contato\n(3)  Editar umcontato\n(4)  buscar um contato pelo Codigo\n(5)  Mostrar lista\n")
        op = int(input())

        match (op):
            case 1: #(1) – inserir um contato

                for i in range(max_pessoas):
                    
                    pessoas[i][0] = input("Informe o codigo da pessoa: ")
                    
                    pessoas[i][1] = input("Informe o numero de telefone da pessoa: ")
                    
                    pessoas[i][2] = input("Informe q idade da pessoa: ")
                    
                    fim = int(input("Deseja inserir mais uma pessoa ? Digite 0 para 'nao' e 1 para 'sim': "))
                    count_pessoas+=1

                    if (fim == 0):
                    
                        break
                    
            case 2: #(2) – Remover um contato
            
                codigo = input("Informe o codigo da pessoa que deseja remover: ")

                for i in range(max_pessoas):

                    if (pessoas[i][0] == codigo):

                        posicao_remover = i

                        for j in range(posicao_remover,max_pessoas - 1):
                        
                            pessoas[j][0] = pessoas[j+1][0]
                            pessoas[j][1] = pessoas[j+1][1]
                            pessoas[j][2] = pessoas[j+1][2]
                        
                            print("Contato removido com sucesso.")
                            count_pessoas-=1# Decrementa o contador de pessoas
                            break# Sai do loop após remover o contato
                
            case 3: #(3) – Editar um contato
                
                codigo = input("Informe o codigo da pessoa que deseja editar: ")

                for i in range(max_pessoas):
                
                    if (pessoas[i][0] == codigo):
                    
                        print("Informe qual campo deseja editar\n\n(1) Codigo\n(2) Telefone\n(3) Idade ")
                        op_1 = int(input())

                        match (op_1):

                            case 1:
                                
                                pessoas[i][0] = input("Informe o novo codigo da pessoa: ")
                                print("Contato editado com sucesso.")
                                
                            case 2:
                                
                                pessoas[i][1] = input("Informe o novo numero de telefone da pessoa: ")
                                print("Contato editado com sucesso.")
                                
                            case 3:
                                
                                pessoas[i][2] = input("Informe a nova idade da pessoa: ")
                                print("Contato editado com sucesso.")
                               
                            case _:
                                print("Valor invalido.")
                        break 
            case 4: #(4) – buscar um contato pelo Código
                
                codigo = input("Informe o codigo da pessoa que deseja buscar: ")

                for i in range(max_pessoas):
                
                    if (pessoas[i][0] == codigo):
                    
                        print(f"{pessoas[i][0]}\n{pessoas[i][1]}\n{pessoas[i][2]}")
            case 5: #(5) – Mostrar lista

                for i in range(count_pessoas):
                
                    print(f"codigo da pessoa: {pessoas[i][0]}")
                    print(f"telefone: {pessoas[i][1]}")
                    print(f"idade: {pessoas[i][2]}")
                
            case _:
                print("Erro: escolha entre 1 a 5.")
    
        if(op > 5 or op < 1):
            continue
        else:
            break
    
    fim = int(input("Deseja realizar mais alguma operacao ? Digite 0 para 'nao' e 1 para 'sim': "))

    if (fim == 0):
        
        break
    
