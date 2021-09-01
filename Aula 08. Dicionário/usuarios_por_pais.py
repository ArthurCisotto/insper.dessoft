def usuarios_por_pais(emails, dicionario):
    dic_paises = {}
    for email in emails:
        usuario = email.split('@')[0]
        pais = email[-2:]
        if dicionario[pais] not in dic_paises:
            dic_paises[dicionario[pais]] = [usuario]
        else:
            dic_paises[dicionario[pais]].append(usuario)
    return dic_paises
