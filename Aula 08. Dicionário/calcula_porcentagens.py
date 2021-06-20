def calcula_porcentagens(dic_erros):
    dic_final = {}
    valores = dic_erros.values()
    soma_total = sum(valores)
    for e in dic_erros.keys():
        dic_final[e] = (dic_erros[e]/soma_total)*100
    return dic_final