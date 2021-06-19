distancia = float(input('Qual a distância em km que você deseja percorrer?'))

if distancia <= 200:
    R = 0.5 * distancia
else:
    R = 100 + (distancia - 200) * 0.45

#print('{0:.2f}'.format(R))
print(f'{R:.2f}')