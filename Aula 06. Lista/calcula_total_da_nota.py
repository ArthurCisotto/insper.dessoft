def calcula_total_da_nota(preco, quantidade):
    lista_final = []
    i = 0
    while i < len(preco):
        lista_final.append(float(preco[i])*float(quantidade[i]))
        i += 1
    soma = 0
    for e in lista_final:
        soma += e 
    return soma
