def agrupa_por_nacionalidade(atletas):
    dic_nacionalidades = {}
    for atleta, dados in atletas.items():
        nacionalidade = dados.get("nacionalidade")
        if nacionalidade not in dic_nacionalidades:
            dic_nacionalidades[nacionalidade] = [atleta]
        else:
            dic_nacionalidades[nacionalidade].append(atleta)
    return dic_nacionalidades
