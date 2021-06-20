def inverte_dicionario(dic):
    dic_invertido = {}
    for nome, idade in dic.items():
        if idade not in dic_invertido.keys():
            dic_invertido[idade] = [nome]
        else:
            dic_invertido[idade].append(nome)
    return dic_invertido