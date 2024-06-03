"""/*5. Faça uma função que recebe por parâmetro o tempo de duração de uma fábrica expressa em segundos e retorna também por parâmetro esse tempo em horas, minutos e segundos.*/
"""

def converteTempo(tempo_em_segundos):

    horas = tempo_em_segundos / 3600   #Calcula o número de horas
    minutos = (tempo_em_segundos % 3600) / 60   #Calcula o número de minutos
    segundos = tempo_em_segundos % 60   #Calcula os segundos restantes

    return horas,minutos,segundos

t_em_s = int(input("Informe o tempo em segundos: "))

tempo = converteTempo(t_em_s)

print(f"Horas: {tempo[0]:.0f}")
print(f"Minutos: {tempo[1]:.0f}")
print(f"Segundos: {tempo[2]:.0f}")