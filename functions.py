from math import pi, sqrt

class Functions:
    def __init__(self, comprimento, gravidade):
        self.Tempo(comprimento, gravidade)

    def Tempo(comprimento, gravidade):
        comprimentoEmCm = comprimento
        L = comprimentoEmCm/100
        g = gravidade
        T = (2 * pi) * sqrt(L / g)
        return T