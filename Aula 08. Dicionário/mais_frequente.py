def conta_ocorrencias(lista):
    dic_ocorrencias = {}
    for palavra in lista:
        if palavra not in dic_ocorrencias.keys():
            dic_ocorrencias[palavra] = lista.count(palavra)
    return dic_ocorrencias

def mais_frequente(lista):
    dic_ocorrencias = conta_ocorrencias(lista)
    for palavra, ocorrencias in dic_ocorrencias.items():
        if ocorrencias == (max(dic_ocorrencias.values())):
            return palavra
