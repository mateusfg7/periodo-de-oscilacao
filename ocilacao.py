from math import pi, sqrt
from sys import argv as param

def Tempo(comprimento):
    comprimentoEmCm = comprimento
    L = comprimentoEmCm/100
    g = 9.8
    T = (2 * pi) * sqrt(L / g)
    print("T={:.2f}s".format(T))

try:
    parametroUm = param[1]
    
    try:
        parametroDois = float(param[2])
    except ValueError:
        print("Valor inválido ou inexistente!")
        exit()

except IndexError:
    print("Número de argumentos insuficientes!")
    exit()

if parametroUm == "t":
    Tempo(parametroDois)