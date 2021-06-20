def aniversariantes_de_setembro(aniversarios):
    dic_setembro = {}
    for nome, data in aniversarios.items():
        if data[4] == '9':
            dic_setembro[nome] = data
    return dic_setembro