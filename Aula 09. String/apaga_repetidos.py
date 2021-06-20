def apaga_repetidos(string):
    termo = ''
    for e in string:
        if e not in termo:
            termo += e
        else:
            termo += '*'
    return termo