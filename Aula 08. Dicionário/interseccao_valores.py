def interseccao_valores(dic1, dic2):
    lista_final = []
    for e in dic1.values():
        if e in dic2.values():
            lista_final.append(e)
    return lista_final
    