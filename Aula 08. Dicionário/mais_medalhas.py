def mais_medalhas(medalhistas):
    dic_final = {}
    for atleta in medalhistas:
        nome = atleta.get("nome")
        nacionalidade = atleta.get("nacionalidade")
        medalhas = atleta.get("ouro") 
        if nacionalidade not in dic_final.keys():
            dic_final[nacionalidade] = medalhas
        else:
            dic_final[nacionalidade] += medalhas
    for nacionalidade, medalhas in dic_final.items():
        if medalhas == (max(dic_final.values())):
            return nacionalidade