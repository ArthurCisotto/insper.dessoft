def entregador_mais_proximo(coord_rest, entregadores):
    distancia_entregadores = []
    for coord in entregadores:
        dist = ((coord[0]-coord_rest[0])**2 + (coord[1]-coord_rest[1])**2)**(1/2)    
        distancia_entregadores.append(dist)
    return distancia_entregadores.index(min(distancia_entregadores))