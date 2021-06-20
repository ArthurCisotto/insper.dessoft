def lista_celulares(lista_telefones):
    lista_final = []
    for e in range(len(lista_telefones)):
        if lista_telefones[e][0] == '+':
            if len(lista_telefones[e]) == 14:
                lista_final.append(lista_telefones[e][5:])
        if len(lista_telefones[e]) == 11:
            lista_final.append(lista_telefones[e][2:])
        if len(lista_telefones[e]) == 9:
            lista_final.append(lista_telefones[e])
    return lista_final