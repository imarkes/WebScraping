from bs4 import BeautifulSoup
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import private


class ScrapingCrash:
    """Cria um array de valores numericos com os resultados obtidos"""

    def __init__(self):
        self.navegador = None
        self.driver = None

        self.configura_driver_de_navegacao()
        self.acessa_urls()
        self.efetua_login()
        self.captura_numeros_sorteados()

    def configura_driver_de_navegacao(self):
        options = Options()
        options.add_argument('window-size=400,800')
        self.navegador = webdriver.Chrome(options=options)
        return self.navegador

    def acessa_urls(self):
        urls = 'https://blaze.com/pt/games/crash'
        self.navegador.get(urls)
        self.driver = self.navegador
        return self.driver

    def efetua_login(self):
        self.entrar = self.driver.find_element(By.CLASS_NAME, "link")
        self.entrar.click()
        sleep(3)

        private.Keys
        input_email = self.driver.find_element(By.TAG_NAME, "input")
        input_email.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[1]/div/input').send_keys(private.Keys)

        private.psw
        input_senha = self.driver.find_element(By.TAG_NAME, "input")
        input_senha.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[2]/div/input').send_keys(private.psw)
        sleep(2)

        submit = self.driver.find_element(By.XPATH, '//*[@id="auth-modal"]/div[2]/form/div[4]/button')
        submit.click()
        sleep(3)

    def captura_numeros_sorteados(self):
        numeros_sorteados = []
        resultado_atual = self.driver.find_element(By.XPATH, '//*[@id="crash-recent"]/div[2]/div/span[1]').text
        resultado_atual = resultado_atual.replace('X', '')

        while True:
            novo_resultado = self.driver.find_element(By.XPATH, '//*[@id="crash-recent"]/div[2]/div/span[1]').text
            novo_resultado = novo_resultado.replace('X', '')

            if resultado_atual != novo_resultado:
                numeros_sorteados.append(novo_resultado)
                print(numeros_sorteados)
                resultado_atual = novo_resultado
            sleep(4)


if __name__ == '__main__':
    ScrapingCrash()
