import math

def reflexao_total_interna(n1, n2, θ2):
    θ_rad = math.radians(θ2)
    senL = (math.sin(θ_rad)*n2)/n1
    if senL > 1:
        return True
    else:
        return False