def pais_campeao(dic_paises):
    ## Confere maior número de medalhas de ouro
    lista_ouros = []
    for medalhas in dic_paises.values():
        lista_ouros.append(medalhas.get("ouro"))
    maior_qtd_ouro = max(lista_ouros)
    
    ## Novo dicionário só com os países que tem a maior quantidade de medalhas de ouro
    dic_prata = {}
    for pais, medalhas in dic_paises.items():
        if medalhas.get("ouro") == maior_qtd_ouro:
            dic_prata[pais] = {
        'prata': medalhas.get("prata"),
        'bronze': medalhas.get("bronze")
    }

    ## Confere maior número de medalhas de prata
    lista_pratas = []
    for medalhas in dic_prata.values():
        lista_pratas.append(medalhas.get("prata"))
    maior_qtd_prata = max(lista_pratas)

    ## Novo dicionário só com os países que tem a maior quantidade de medalhas de ouro e prata
    dic_bronze= {}
    for pais, medalhas in dic_prata.items():
        if medalhas.get("prata") == maior_qtd_prata:
            dic_bronze[pais] = {
        'bronze': medalhas.get("bronze")
    }

    ## Confere maior número de medalhas de bronze
    lista_bronzes = []
    for medalhas in dic_bronze.values():
        lista_bronzes.append(medalhas.get("bronze"))
    maior_qtd_bronze = max(lista_bronzes)

    ## Confere país que que tem a maior quantidade de medalhas de ouro, prata e bronze
    dic_bronze= {}
    for pais, medalhas in dic_prata.items():
        if medalhas.get("bronze") == maior_qtd_bronze:
            return pais
