def acha_bigramas(string):
    lista_final = []
    i = 0 
    while i < len(string)-1:
        bigrama = string[i:i+2]
        lista_final.append(bigrama)
        i+=1 
    return lista_final

def conta_bigramas(string):
    dic_ocorrencias = {}
    lista_bigramas = acha_bigramas(string)
    for bigrama in lista_bigramas:
        if bigrama not in dic_ocorrencias.keys():
            dic_ocorrencias[bigrama] = lista_bigramas.count(bigrama)
    return dic_ocorrencias

