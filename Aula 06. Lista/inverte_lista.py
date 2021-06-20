def inverte_lista(lista):
    termos_lista = len(lista)
    posicao = termos_lista - 1
    lista_invertida = []
    while termos_lista >= 1:
        lista_invertida.append(lista[posicao])
        termos_lista -= 1
        posicao -= 1
    return lista_invertida
