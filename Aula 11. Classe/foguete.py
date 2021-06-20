class Foguete:
    tempo = 0
    def __init__(self, velocidade):
        self.velocidade = velocidade
    def atualizar(self, tempo):
        self.tempo += tempo
        deslocamento = self.tempo/3600 * self.velocidade 
        return deslocamento



