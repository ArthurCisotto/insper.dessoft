def estritamente_crescente(lista):
    if len(lista) == 0:
        return []
    termo_maior = lista[0]
    lista_final = [termo_maior]
    i = 1
    while i < len(lista):
        if termo_maior < lista[i]:
            lista_final.append(lista[i])
            termo_maior = lista[i]
        i += 1
    return lista_final
    
