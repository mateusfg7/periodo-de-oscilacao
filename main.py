from sys import argv as param

from identificar_astro import Main
from functions import Functions as func

def Menu():
    print("\nUse: ocilacao.py [calculo] [astro] [base]")
    
    print("\nCalculo")
    print("""
    t   tempo de ocilação
    c   comprimento do pêndulo
    """)
    
    print("\nAstro")
    print("""
    sol   Sol
    mer   Mercúrio
    ven   Venus
    ter   Terra
    mar   Marte
    jup   Júpiter
    sat   Saturno
    ura   Urano
    net   Netuno
    plu   Plutão
    lua   Lua
    """)

    print("\nBase")
    print("""
    Comprimento da corda em centímetros para retornar o tempo de ocilação.
    Tempo de ocilação em segundos para retornar o comprimento da corda.
    """)

    print("\nhelp   retornar esse menu")


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



astro = Main.astro(parametroDois)


if parametroUm == "t":
    output = func.Tempo(parametroTres, astro)
    print("T ≅ {:.5f}s".format(output))

elif parametroUm == "c":
    output = func.Comprimento(parametroTres, astro)
    print("L ≅ {:.5f}s".format(output))

elif parametroUm == "help":
    Menu()