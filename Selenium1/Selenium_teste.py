from selenium import webdriver
from pathlib import Path
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
From dados import Meu_email, Minha_senha

Raiz = Path(__file__).parent.parent
Pasta_driver = Raiz / 'Selenium1' / 'chromedriver'


class ChromeAuto:
    def __init__(self):
        self.service = Service(executable_path=str(Pasta_driver))
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=c:\\Selenium1\\Perfil')
        self.chrome = webdriver.Chrome(
            service=self.service,
            options=self.options
        )

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element(By.LINK_TEXT, 'Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro:', e)

    def status(self):
        try:
            btn_logout = self.chrome.find_element(By.CSS_SELECTOR,
                                                  'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > summary > img')
            btn_logout.click()
        except Exception as e:
            print("error no logout:", e)

    def click_logout(self):
        try:
            btn_sign_out = self.chrome.find_element(By.CSS_SELECTOR,
                                                    'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
            btn_sign_out.click()
        except Exception as e:
            print('Error no click', e)

    def login(self):
        try:
            self.chrome.find_element(By.NAME, 'login').send_keys(Meu_email)
            self.chrome.find_element(By.NAME, 'password').send_keys(Minha_senha)
            self.chrome.find_element(By.NAME, 'commit').click()
        except Exception as e:
            print('error:', e)


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com')
    sleep(1)
    chrome.status()
    sleep(3)
    chrome.click_logout()
    sleep(1)
    chrome.clica_sign_in()
    sleep(1)
    chrome.login()
    sleep(1)
    chrome.sair()
