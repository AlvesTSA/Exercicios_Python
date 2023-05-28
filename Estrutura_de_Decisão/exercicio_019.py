#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = 0
mes = 0
ano = 0
data = True

print("Informe uma data dd/mm/aaaa: ")
entrada = input()
dia, mes, ano = map(int, entrada.split("/"))

if ano < 0:

    data = False

elif mes <= 0 or mes > 12:

    data = False

elif dia <= 0 or dia > 31:

    data = False

elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:

    data = False

elif mes == 2:

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):

        if dia > 29:
            data = False

    else:

        if dia > 28:
            data = False

if data:

    print("Data: {:02d}/{:02d}/{:04d}".format(dia, mes, ano))

else:

    print("Data inválida! Tente novamente.")

#Primeiro, a mensagem "Informe uma data dd/mm/aaaa: " é exibida na tela usando a função print(). Em seguida, a função input() é chamada para aguardar a entrada do usuário.

#Quando o usuário insere a data no formato "dd/mm/aaaa" e pressiona Enter, a entrada é armazenada na variável entrada como uma string.

#Em seguida, a função split("/") é usada para dividir a string entrada em partes separadas pelo caractere "/". Isso cria uma lista de strings contendo os valores do dia, mês e ano.

#A função map(int, ...) é usada para aplicar a função int() a cada elemento da lista. Isso converte cada valor do dia, mês e ano de string para inteiro.

#Por fim, os valores convertidos são atribuídos às variáveis dia, mes e ano, respectivamente. Agora, essas variáveis contêm os valores numéricos correspondentes à data fornecida pelo usuário.


