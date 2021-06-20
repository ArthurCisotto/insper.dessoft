def total_do_semestre_por_bairro(gasto_12):
    gasto_6 = {}
    for bairro, gastos in gasto_12.items():
        gasto_6[bairro] = sum(gastos[6:])
    return gasto_6
