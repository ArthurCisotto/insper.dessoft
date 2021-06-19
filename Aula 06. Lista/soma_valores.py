def soma_valores(lista):
    termos_lista = len(lista)
    posicao = termos_lista - 1
    soma = 0
    while termos_lista >= 1:
        soma += lista[posicao]
        termos_lista -= 1
        posicao -= 1
    return soma
