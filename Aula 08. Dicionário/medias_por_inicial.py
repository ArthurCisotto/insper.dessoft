def medias_por_inicial(nomes_e_notas):
    dic_letras = {}
    for nome, nota in nomes_e_notas.items():
        if nome[0] not in dic_letras.keys():
            dic_letras[nome[0]] = [nota]
        else:
            dic_letras[nome[0]].append(nota)
    dic_medias = {}
    for inicial, notas in dic_letras.items():
        dic_medias[inicial] = sum(notas)/len(notas)
    return dic_medias