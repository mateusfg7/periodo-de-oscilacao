import json

class carregar_astros:

    def __init__(self):
        self.carregar_astros()

    def carregar_astros():
        arquivoJson = open('astros.json', 'r')
        astro = json.loads(arquivoJson.read())
        arquivoJson.close()
        return astro