import math

def area_pentagono(lado):
    ang_rad = math.radians(36)
    apotema = lado/(2*math.tan(ang_rad))
    area = 5 * (apotema * lado)/2
    return area