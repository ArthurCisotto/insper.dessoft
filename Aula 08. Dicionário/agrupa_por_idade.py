def agrupa_por_idade(dic):
    dic_final = {'criança': [], 'adolescente': [], 'adulto': [], 'idoso': []}
    for nome, idade in dic.items():
        if idade >= 60:
            dic_final['idoso'].append(nome)
        elif idade >= 18:
            dic_final['adulto'].append(nome)
        elif idade >= 12:
            dic_final['adolescente'].append(nome)
        else:
            dic_final['criança'].append(nome) 
    return dic_final

