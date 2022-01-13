from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class ScrapingCrash:
    """Captura o os numeros sorteados e exporta para um arquivo csv"""

    def __init__(self):
        self.driver = None
        self.navegador = None
        self.numeros_sorteados = []

        self.configura_driver_de_navegacao()
        self.acessa_urls()
        self.captura_numeros_sorteados()
        self.cria_csv_com_resultados()
        self.sair_da_aplicacao()

    def configura_driver_de_navegacao(self):
        options = Options()
        options.add_argument('window-size=400,500')
        self.navegador = webdriver.Chrome(options=options)
        return self.navegador

    def acessa_urls(self):
        urls = 'https://blaze.com/pt/games/crash'
        self.navegador.get(urls)
        self.driver = self.navegador
        return self.driver

    def captura_numeros_sorteados(self):

        resultado_atual = self.driver.find_element(By.XPATH, '//*[@id="crash-recent"]/div[2]/div/span[1]').text
        resultado_atual = resultado_atual.replace('X', '')

        contador = 0
        while contador <= 300:
            novo_resultado = self.driver.find_element(By.XPATH, '//*[@id="crash-recent"]/div[2]/div/span[1]').text
            novo_resultado = novo_resultado.replace('X', '')

            if resultado_atual != novo_resultado:

                self.numeros_sorteados.append({'numero': novo_resultado})
                print(self.numeros_sorteados)
                resultado_atual = novo_resultado

                contador += 1

    def cria_csv_com_resultados(self):
        df = pd.DataFrame(self.numeros_sorteados)
        df.to_csv('./numeros_sorteados3.csv', sep=',', encoding='utf-8')

    def sair_da_aplicacao(self):
        self.driver.quit()


if __name__ == '__main__':
    ScrapingCrash()

