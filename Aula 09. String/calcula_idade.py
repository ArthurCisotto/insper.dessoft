def calcula_idade(nascimento, atual):
    if int(atual[3:5]) > int(nascimento[3:5]):
        return (int(atual[6:])-int(nascimento[6:]))
    if int(atual[3:5]) == int(nascimento[3:5]) and int(atual[:2]) >= int(nascimento[:2]):
        return (int(atual[6:])-int(nascimento[6:]))
    else:
        return (int(atual[6:])-int(nascimento[6:]))-1
