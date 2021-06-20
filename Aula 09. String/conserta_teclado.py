def conserta_teclado(palavra_errada):
    palavra_errada = palavra_errada.lower()
    palavra_consertada = palavra_errada[:1]
    for e in range(len(palavra_errada)-1):
        if palavra_errada[e+1] != palavra_errada[e]:
            palavra_consertada += palavra_errada[e+1]
    return palavra_consertada
