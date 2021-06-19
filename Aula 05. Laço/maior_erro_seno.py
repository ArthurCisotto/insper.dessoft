import math

x = 0
erro = 0
maior_erro = 0
angulo = 0
while x<=90:
    sin = (4*x*(180-x))/(40500-x*(180-x))
    sin2 = math.sin(math.radians(x))
    erro = abs(sin-sin2)
    if erro > maior_erro:
        maior_erro = erro 
        angulo = x
    x+=1

print(angulo)
