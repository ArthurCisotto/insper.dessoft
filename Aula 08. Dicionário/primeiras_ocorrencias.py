def primeiras_ocorrencias(string):
    dic = {}
    for letra in string:
        if letra not in dic.keys():
            dic[letra] = string.find(letra)
    return dic