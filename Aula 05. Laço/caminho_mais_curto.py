def caminho_mais_curto(caminhos):
    lista_distancias = []
    for caminho in caminhos:
        dist = 0
        i = 0
        while i < len(caminho)-1:
            dist += ((caminho[i][0]-caminho[i+1][0])**2 + (caminho[i][1]-caminho[i+1][1])**2)**(1/2)    
            i+=1
        lista_distancias.append(dist)
    return caminhos[lista_distancias.index(min(lista_distancias))]
