def calcula_norma(vetor):
    i = 0
    soma = 0
    while i < len(vetor):
        termo = (vetor[i])**2
        soma += termo
        i += 1
    return soma**(1/2)