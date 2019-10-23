from math import pi, sqrt

class Functions:
    
    def __init__(self, comprimento, tempo, gravidade):
        self.Tempo(comprimento, gravidade)
        self.Comprimento(tempo, gravidade)

    def Tempo(comprimento, gravidade):
        comprimentoEmCm = comprimento
        L = comprimentoEmCm/100
        g = gravidade
        T = (2 * pi) * sqrt(L / g)
        return T

    def Comprimento(tempo, gravidade):
        g = gravidade
        T = tempo
        L = (T/4*(pi**2))*g
        return L