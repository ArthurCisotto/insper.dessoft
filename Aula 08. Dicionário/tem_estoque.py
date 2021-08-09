def tem_estoque(dic_pecas, dic_estoque):
    erros = 0
    for peca, qtd in dic_pecas.items():
        if peca not in dic_estoque.keys():
            erros+=1
        else:
            if dic_estoque[peca] < qtd:
                erros +=1
    if erros == 0:
        return True
    else:
        return False
