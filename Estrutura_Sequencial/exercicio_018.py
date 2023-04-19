#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

mb = 0 
mbps = 0
t = 0

print("Informe o tamanho do arquivo: ")
mb = float(input())

print("Informe a velocidade do link: ")
mbps = float(input())

t = mb/mbps

print("Tempo para dowloading: {}".format(t))

