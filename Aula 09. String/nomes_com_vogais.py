def nomes_com_vogais(nomes):
    vogais = ['A', 'I', 'U', 'E', 'O']
    counter_vogais = 0
    counter_conso = 0
    for e in nomes:
        if e[0] in vogais:
            counter_vogais += 1
        else:
            counter_conso += 1
    lista_final = [counter_vogais, counter_conso]
    return lista_final
