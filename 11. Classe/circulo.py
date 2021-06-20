class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def contem(self, ponto):
        distancia = ((ponto.x - self.centro.x)**2 + (ponto.y - self.centro.y)**2)**(1/2)
        if distancia <= self.raio:
            return True
        else:
            return False
