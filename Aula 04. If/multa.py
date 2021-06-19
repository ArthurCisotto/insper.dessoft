vel = float(input('Qual é a velocidade do carro?'))
multa = 5 * (vel-80)

if vel > 80:
    print('Você foi multado em {0:.2f} reais'.format(multa))
else:
    print('Não foi multado')