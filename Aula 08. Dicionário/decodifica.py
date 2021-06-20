def decodifica(codigo, cifra):
    palavra_decifrada = ''
    for letra in codigo:
        if letra not in cifra.values():
            palavra_decifrada += letra
        else:
            for orig, cod in cifra.items():
                if letra == cod:
                    palavra_decifrada += orig
    return palavra_decifrada