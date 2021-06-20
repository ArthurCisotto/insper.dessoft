def monta_dicionario(lista1, lista2):
    dicionario = {}
    for e in range(len(lista1)):
        dicionario[lista1[e]] = lista2[e]
    return dicionario     