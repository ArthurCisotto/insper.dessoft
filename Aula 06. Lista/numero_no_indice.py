def numero_no_indice(lista):
    lista_final = []
    i = 0
    while i < len(lista):
        if i == lista[i]:
            lista_final.append(lista[i])
        i += 1 
    return lista_final