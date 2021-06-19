def pacotes_correio(pacotes):
    for e in range(len(pacotes)):
        if pacotes[e][0] != len(pacotes):
            return "pacote perdido"
        if pacotes[e][1] != e+1:
            return "ordem errada"
        tamanho_padrao = pacotes[0][2]
        if pacotes[e][2] != tamanho_padrao:
            return "tamanho errado"
    return "tudo certo"