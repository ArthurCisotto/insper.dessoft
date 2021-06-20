def promocao_viagens(destinos):
    dic_final = {}
    for destino, lista in destinos.items():
        valor = lista[1]-(lista[0]*0.1*lista[1])
        dic_final[destino] = valor
    return dic_final