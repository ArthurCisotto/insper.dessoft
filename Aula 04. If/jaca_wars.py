import math

v = float(input('Qual é a velocidade?'))
O = float(input('Qual é o ângulo de lançamento?'))
O_rad = math.radians(O)
g = 9.8

d = (v**2) * math.sin(2*O_rad) / g

if d < 98:
    print('Muito perto')
else:
    if d >= 98 and d <= 102:
        print('Acertou!')
    else:
        print('Muito longe')
