def filtra_bagagens(lista, alt_limite, larg_limite, prof_limite):
    i = 0
    bag_excedentes = 0
    while i < len(lista):
        if lista[i][0] > alt_limite or lista[i][1] > larg_limite or lista[i][2] > prof_limite:
            bag_excedentes += 1
        i += 1
    return bag_excedentes 