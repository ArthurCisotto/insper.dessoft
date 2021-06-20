def traduz(lista, dic):
    lista_final = []
    for palavra in lista:
        for ingles, port in dic.items():
            if palavra == ingles:
                lista_final.append(port)
    return lista_final
