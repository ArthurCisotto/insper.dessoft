def tamanho_minimo(string, n):
    lista_final = []
    lista = string.split(' ')
    for e in lista:
        if len(e) > n:
            lista_final.append(e)
    return lista_final