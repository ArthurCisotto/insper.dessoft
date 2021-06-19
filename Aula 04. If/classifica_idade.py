def classifica_idade(idade):
    if idade <= 11:
        return 'crianca'
    else:
        if idade >= 12 and idade <= 17:
            return 'adolescente'
        else:
            return 'adulto'
