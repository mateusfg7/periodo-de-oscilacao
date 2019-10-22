from math import pi, sqrt
from sys import argv as param

def Tempo(comprimento):
    comprimentoEmCm = comprimento
    L = comprimentoEmCm/100
    g = 9.8
    T = (2 * pi) * sqrt(L / g)
    print("T ≅ {:.2f}s".format(T))

def Comprimento(tempo):
    g = 9.8
    T = tempo
    L = (T/4*(pi**2))*g
    print("L ≅ {:.2f}cm".format(L))

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
elif parametroUm == "c":
    Comprimento(parametroDois)