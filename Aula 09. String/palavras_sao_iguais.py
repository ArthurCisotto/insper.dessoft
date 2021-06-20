def palavras_sao_iguais(string):
    if '-' in string:
        palavras = string.split('-')
        if palavras[0] == palavras[1]:
            return True
        else:
            return False
    else:
        return False