def acha_bigramas(string):
    lista_final = []
    i = 0 
    while i < len(string)-1:
        bigrama = string[i:i+2]
        lista_final.append(bigrama)
        i+=1
    for e in lista_final:
        if lista_final.count(e) > 1:
            lista_final.remove(e) 
    return lista_final