import math

def snell_descartes(n1, n2, θ1):
    rad_θ1 = math.radians(θ1)
    sen_θ2 = n1 * math.sin(rad_θ1)/n2
    θ2 = math.asin(sen_θ2)
    return math.degrees(θ2)