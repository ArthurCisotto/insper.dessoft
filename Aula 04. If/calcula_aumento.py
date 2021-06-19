def calcula_aumento(salario):
    salariof = float(salario)
    if salariof > 1250:
        aumento = salariof * 0.10
    else:
        aumento = salariof * 0.15
    return aumento
