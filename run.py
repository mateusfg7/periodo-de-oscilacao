from sys import argv as param

from menu import Menu
from identificar_astro import Main
from functions import Functions as func




try:
    parametroUm = param[1]
    if parametroUm != 'help':
        parametroDois = param[2]
        parametroTres = float(param[3])
except IndexError:
    print("Número de argumentos insuficientes!")
    Menu()
    exit()
except ValueError:
        print("Valor inválido ou inexistente!")
        Menu()
        exit()


try:
    astro = Main.astro(parametroDois)
except NameError:
    None


if parametroUm == "t":
    output = func.Tempo(parametroTres, astro)
    print("T ≅ {:.5f}s".format(output))

elif parametroUm == "c":
    output = func.Comprimento(parametroTres, astro)
    print("L ≅ {:.5f}s".format(output))

elif parametroUm == "help":
    Menu()