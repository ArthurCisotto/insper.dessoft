def interseccao_chaves(dic1, dic2):
    lista_final = []
    for e in dic1.keys():
        if e in dic2.keys():
            lista_final.append(e)
    return lista_final
    