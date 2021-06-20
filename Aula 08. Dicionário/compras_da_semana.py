def compras_da_semana(receitas, pratos):
    dic_compras = {}
    for prato in pratos:
        ingredientes = receitas.get(prato)
        for i, q in ingredientes.items():
            if i not in dic_compras:
                dic_compras[i] = q
            else:
                dic_compras[i]+=q
    return dic_compras