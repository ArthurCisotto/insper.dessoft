def dias_do_ano(data):
    dias = int(data[:2]) - 1
    mes = int(data[3:5])
    dias_nos_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    soma = dias
    for e in range(mes-1):
        soma += dias_nos_meses[e]
    return soma
