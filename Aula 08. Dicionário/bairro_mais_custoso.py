def total_do_semestre_por_bairro(gasto_12):
    gasto_6 = {}
    for bairro, gastos in gasto_12.items():
        gasto_6[bairro] = sum(gastos[6:])
    return gasto_6

def bairro_mais_custoso(bairros_e_gastos):
    gastos_totais = total_do_semestre_por_bairro(bairros_e_gastos)
    for bairro, gasto in gastos_totais.items():
        if gasto == (max(gastos_totais.values())):
            return bairro
        
