from flask import Flask, request,redirect,render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import bot

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')
@app.route('/bot')
def bot():

    class ChromeAuto():
        def __init__(self):
            self.drive_path = 'chromedriver'
            # aqui salva o perfil
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("user-data-dir=C:/Users/IGOR/Documents/guithub/projetocomselenium/Perfil")
            # aqui instancia o navegador
            self.chrome = webdriver.Chrome(
                self.drive_path,
                options=self.options
            )

        def seguir(self):
            try:
                btnseguir = self.chrome.find_element_by_partial_link_text('Seguir')
            except:
                pass
        # def logout(self):
        #     logout = self.chrome.find_element_by_css_selector(
        #         'body > div.position-relative.js-header-wrapper > header > div.Header-item.position-relative.mr-0.d-none.d-md-flex > details > details-menu > form > button')
        #     logout.click()

        def acessa(self, site):
            self.chrome.get(site)

        def sair(self):
            self.chrome.quit()

    if __name__ == '__main__':
        chrome = ChromeAuto()
        chrome.acessa('https://www.instagram.com')
        sleep(20)
        chrome.acessa('https://www.instagram.com/igormarinhos')
        sleep(1)
        chrome.seguir()
        sleep(2)
        chrome.sair()
        # chrome.clicaLogin()
        # sleep(3)
        # chrome.faz_login()
        # sleep(2)
        # chrome.clicaPerfil()
        # sleep(3)
        # chrome.logout()
        #
        # sleep(2)
        # chrome.sair()

        return render_template('bot.html')
if __name__ == '__main__':
    app.run(debug=True)
