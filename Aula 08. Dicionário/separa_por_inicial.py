def separa_por_inicial(salas):
    lista_nomes = []
    for nomes in salas.values():
        lista_nomes+=nomes
    dic_letras = {}
    for nome in lista_nomes:
        if nome[0] not in dic_letras.keys():
            dic_letras[nome[0]] = [nome]
        else:
            dic_letras[nome[0]].append(nome)
    return dic_letras