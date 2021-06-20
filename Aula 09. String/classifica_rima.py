def classifica_rima(a, b, c, d):
    if a == c and b == d and a != b:
        return 'alternada'
    if a == d and b == c and a != b:
        return 'interpolada'
    if a == b and c == d and a != c:
        return 'emparelhada'
    else:
        return 'outra'