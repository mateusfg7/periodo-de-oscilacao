from sys import argv as param

from lib.menu import *
from lib.astro import *
from lib.functions import *

from carregar_json import carregar_astros as astros

try:
    parametroUm = param[1]
    if parametroUm != 'help':
        parametroDois = param[2]
        parametroTres = float(param[3])
except IndexError:
    print("Número de argumentos insuficientes!")
    menu()
    exit()
except ValueError:
        print("Valor inválido ou inexistente!")
        menu()
        exit()


try:
    loadAstros = astros.carregar_astros()
    astro = astro(parametroDois, loadAstros)
except NameError:
    None


if parametroUm == "t":
    output = tempo(parametroTres, astro)
    print("T ≅ {:.5f}s".format(output))

elif parametroUm == "c":
    output = comprimento(parametroTres, astro)
    print("L ≅ {:.5f}s".format(output))

elif parametroUm == "help":
    menu()