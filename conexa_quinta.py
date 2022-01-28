
from selenium import webdriver

#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time, send_mail


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
#wd = webdriver.Chrome(ChromeDriverManager().install())


def navigate_thursday():
    try:
        wd.get('https://app.conexasaude.com.br/')
        time.sleep(8)
        email = wd.find_element_by_xpath('//*[@id="email"]')
        email.send_keys('seu@email.com')
        senha = wd.find_element_by_xpath('//*[@id="senha"]')
        senha.send_keys('1234SuaSenha')
        botao_entrar = wd.find_element_by_xpath('//*[@id="submit"]')
        botao_entrar.click()
        time.sleep(8)
        wd.get('https://app.conexasaude.com.br/horarios')
        time.sleep(8)
        botao_adicionar_horario = wd.find_element_by_xpath('/html/body/div[8]/div[5]/div/div[3]/div/div/div[2]/button')
        botao_adicionar_horario.click()
        time.sleep(3)
        campo_horario_inicio = wd.find_element_by_xpath('/html/body/div[8]/div[5]/div/div[3]/div/div/div[1]/div/div[1]/div/input')
        campo_horario_inicio.send_keys('1400')
        time.sleep(1)
        campo_horario_termino = wd.find_element_by_xpath('/html/body/div[8]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div/input')
        campo_horario_termino.send_keys('1900')
        time.sleep(1)
        try:
            botao_excluir_horario_quinta = wd.find_element_by_xpath('/html/body/div[8]/div[5]/div/div[4]/div/div/div[1]/div/div[3]/a')
            botao_excluir_horario_quinta.click()
            time.sleep(2)
        except:
            botao_excluir_horario_quinta = wd.find_element_by_xpath('/html/body/div[8]/div[5]/div/div[4]/div/div/div[1]/div/div[3]/a/img')
            botao_excluir_horario_quinta.click()
            time.sleep(2)
    except:
        time.sleep(180)
        try:
            wd.get('https://app.conexasaude.com.br/')
            time.sleep(8)
            email = wd.find_element_by_xpath('//*[@id="email"]')
            email.send_keys('andre@franciscatto.com')
            senha = wd.find_element_by_xpath('//*[@id="senha"]')
            senha.send_keys('1234@Unimed')
            botao_entrar = wd.find_element_by_xpath('//*[@id="submit"]')
            botao_entrar.click()
            time.sleep(8)
            wd.get('https://app.conexasaude.com.br/horarios')
            time.sleep(8)
            # botão excluir horário da tarde
            botao_adicionar_horario = wd.find_element_by_xpath(
                '/html/body/div[8]/div[5]/div/div[3]/div/div/div[2]/button')
            botao_adicionar_horario.click()
            time.sleep(3)
            campo_horario_inicio = wd.find_element_by_xpath(
                '/html/body/div[8]/div[5]/div/div[3]/div/div/div[1]/div/div[1]/div/input')
            campo_horario_inicio.send_keys('1400')
            time.sleep(1)
            campo_horario_termino = wd.find_element_by_xpath(
                '/html/body/div[8]/div[5]/div/div[3]/div/div/div[1]/div/div[2]/div/input')
            campo_horario_termino.send_keys('1900')
            time.sleep(1)
            try:
                botao_excluir_horario_quinta = wd.find_element_by_xpath(
                    '/html/body/div[8]/div[5]/div/div[4]/div/div/div[1]/div/div[3]/a/img')
                botao_excluir_horario_quinta.click()
                time.sleep(2)
            except:
                botao_excluir_horario_quinta = wd.find_element_by_xpath(
                    '/html/body/div[8]/div[5]/div/div[4]/div/div/div[1]/div/div[3]/a')
                botao_excluir_horario_quinta.click()
                time.sleep(2)
        except Exception as err:
            send_mail.sendmail(err, 'afmaster@gmail.com')



