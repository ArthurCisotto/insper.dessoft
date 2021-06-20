def calcula_escola(notas):
    i = 0
    while i < 9:
        notas[i].remove(min(notas[i]))
        i += 1
    soma = 0
    c = 0
    while c < 9:
        for e in notas[c]:
            soma += e
        c += 1
    return soma