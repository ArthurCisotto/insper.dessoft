def calcula_media(atletas, pais):
    idade_paises = {}
    for atleta, dados in atletas.items():
        nacionalidade = dados.get("nacionalidade")
        idade = dados.get("idade")
        if nacionalidade not in idade_paises:
            idade_paises[nacionalidade] = [idade]
        else:
            idade_paises[nacionalidade].append(idade)   
    media_pais = sum(idade_paises[pais])/len(idade_paises[pais])
    return media_pais
