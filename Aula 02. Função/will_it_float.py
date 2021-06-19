import math

def will_it_float(P, R, r):
    vol = 2*((math.pi)**2)*(R/100)*((r/100)**2)
    d = P/vol 
    if d <= 997:
        return True
    else:
        return False

    