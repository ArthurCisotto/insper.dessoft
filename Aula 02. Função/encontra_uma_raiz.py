import math
def encontra_uma_raiz(a,b,c):
    delta = ((b**2) - (4*a*c))
    x = (-b + math.sqrt(delta))/(2*a) 
    return x