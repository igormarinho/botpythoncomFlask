from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class ChromeAuto():
    def __init__(self):
        self.drive_path = 'chromedriver'
        # aqui salva o perfil
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user=data-dir=Perfil')
        # aqui instancia o navegador
        self.chrome = webdriver.Chrome(
            self.drive_path,
            options = self.options
        )
    def clicaLogin(self):
        try:
            btnsingin = self.chrome.find_element_by_link_text('Sign in')
            btnsingin.click()
        except Exception as e:
            print('Erro ao clicar no sign in ')

    def faz_login(self):
        try:
            inputLogin = self.chrome.find_element_by_id('login_field')
            inputPassword = self.chrome.find_element_by_id('password')
            btnlogin = self.chrome.find_element_by_name('commit')
            inputLogin.send_keys('igormarinhosilva@gmail.com')
            inputPassword.send_keys('37192541aa')
            sleep(3)
            btnlogin.click()

        except Exception as e:
            print('Erro ao fazer login')


    def clicaPerfil(self):
        try:
            perfil = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details')
            perfil.click()
        except Exception as e:
            print('erro ao clicar no perfil')
    def logout(self):
        logout = self.chrome.find_element_by_css_selector('body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
        logout.click()
    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

if __name__ =='__main__':
    chrome = ChromeAuto()
    chrome.acessa('https://github.com/')
    chrome.clicaLogin()
    sleep(3)
    chrome.faz_login()
    sleep(2)
    chrome.clicaPerfil()
    sleep(3)
    chrome.logout()

    sleep(2)
    chrome.sair()
