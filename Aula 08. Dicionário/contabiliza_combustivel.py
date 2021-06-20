def contabiliza_combustivel(dic):
    dic_medio = {}
    dic_final = {}
    for gastos in dic.values():
        tipo = gastos.get('tipo')
        litros = gastos.get('litros')
        custo = gastos.get('custo')
        if tipo not in dic_medio.keys():
            dic_medio[tipo] = {'total litros': [litros],'custo total': [custo]}
        else:
            dic_medio[tipo]['total litros'].append(litros)
            dic_medio[tipo]['custo total'].append(custo)
    for tipo, info in dic_medio.items():
        dic_final[tipo] = {'total litros': sum(info['total litros']),'custo por litro': sum(info['custo total'])/sum(info['total litros'])}
    return dic_final
