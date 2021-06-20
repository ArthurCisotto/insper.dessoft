def calcula_tempo(atletas):
    dic_tempo = {}
    for atleta in atletas:
        a = atletas[atleta]
        t = (200/a)**(1/2)
        dic_tempo[atleta] = t
    return dic_tempo
