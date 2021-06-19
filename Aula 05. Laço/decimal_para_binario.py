def decimal_para_binario(decimal):
    binario = ''
    if decimal < 0:
        return 'Negativo'
    else:
        while decimal > 0:
            resto = decimal%2
            decimal = decimal//2
            binario = str(resto) + binario
    return binario