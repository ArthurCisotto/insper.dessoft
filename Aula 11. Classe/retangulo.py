class Retangulo:
    def __init__(self, ponto1, ponto2):
        self.altura = ponto2.y - ponto1.y
        self.largura = ponto2.x - ponto1.x
    def calcula_perimetro(self):
        return (2*self.altura+2*self.largura)
    def calcula_area(self):
        return self.altura*self.largura
