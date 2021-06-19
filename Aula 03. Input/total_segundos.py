dias = int(input('Qual é a quantidade de dias?'))
horas = int(input('Qual é a quantidade de horas?'))
minutos = int(input('Qual é a quantidade de minutos?'))
segundos = int(input('Qual é a quantidade de segundos?'))

total_segundos = segundos + 60 * minutos + 3600 * horas + 86400 * dias
print(total_segundos)

