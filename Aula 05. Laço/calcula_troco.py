
def calcula_troco(compra, pagamento, notas):
    valor_troco = pagamento - compra
    lista_final = []
    while valor_troco > 0:
        i = 0
        while i < len(notas):
            if valor_troco < notas[i]:
                i+=1
            else:
                num_notas = int(valor_troco/notas[i]) 
                valor_troco = valor_troco - num_notas*notas[i]
                if notas[i] >= 2:
                    lista_final.append(f'{num_notas} nota(s) de R$ {notas[i]}')
                else:
                    lista_final.append(f'{num_notas} moeda(s) de R$ {notas[i]}') 

    return lista_final