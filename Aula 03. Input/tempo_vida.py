num_cig = int(input('Quantos cigarros você fuma por dia?'))
anos = int(input('Há quantos anos você fuma'))
#1440 é a quantidade de minutos em um dia
tempo = num_cig*(10/1440)*anos*365
print(tempo)
