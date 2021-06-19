import math

def calcula_distancia_do_projetil(v, θ, y0):
    g = 9.8
    d = ((v**2)/(2*g))*(1 + (1 + ((2*g*y0)/((v**2)*(math.sin(θ))**2)))**(1/2))*math.sin(2 * θ)
    return d

