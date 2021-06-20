def lista_caracteres(string):
    lista_final = []
    for e in range(len(string)):
        if string[e] not in lista_final:
            lista_final.append(string[e])  
    return lista_final 