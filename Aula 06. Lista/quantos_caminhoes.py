def quantos_caminhoes(pesos):
    num_caminhoes = 0
    soma = pesos[0]
    for c in range(len(pesos)-1):
        soma += pesos[c+1]
        if soma> 2000:
            num_caminhoes += 1
            soma = pesos[c+1]
        if soma == 2000:
            num_caminhoes += 1
            soma = 0
    if soma > 0:
        num_caminhoes += 1
    return num_caminhoes

