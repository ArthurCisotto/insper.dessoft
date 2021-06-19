def eh_bissexto(ano):
    if (ano % 4) == 0:
        if (ano % 100) == 0: 
            if (ano % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    return False

def valida_data(dia, mes, ano):
    max_dias = 0
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        max_dias = 31
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        max_dias = 30
    if mes == 2:
        if eh_bissexto(ano):
            max_dias = 29
        else:
            max_dias = 28
    if dia > max_dias:
        return False
    else:
        return True