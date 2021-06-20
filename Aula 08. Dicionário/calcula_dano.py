def calcula_dano(atributos):
    forca = atributos.get("força")
    equipamentos = atributos.get("equipamentos")
    dano = forca
    for equipamento in equipamentos:
        dano += equipamento.get("força")
    return dano
