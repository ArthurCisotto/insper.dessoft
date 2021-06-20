def junta_nome_sobrenome(nomes, sobrenomes):
    lista_final = []
    i = 0
    while i < len(nomes):
        lista_final.append(nomes[i] + ' ' + sobrenomes[i])
        i += 1
    return lista_final