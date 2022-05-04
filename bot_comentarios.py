import time
from multiprocessing.connection import wait

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def executar_login():
    navegador.get("https://www.instagram.com")
    time.sleep(3)
    campo_usuario = navegador.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[1]/div/label/input')
    campo_usuario.click()
    time.sleep(3)
    campo_usuario.send_keys("usuario")
    time.sleep(3)
    campo_senha = navegador.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[2]/div/label/input')
    campo_senha.click()
    time.sleep(3)
    campo_senha.send_keys("senhausuario")
    time.sleep(3)
    campo_senha.send_keys(Keys.ENTER)
    time.sleep(3)


def inserir_comentario(comentario, repeticoes):
    for x in range(repeticoes):
        navegador.get('Link da Postagem')
        time.sleep(3)
        campo_comentario = wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, '//div[@class="RxpZH"]')
            )
        )
        campo_comentario.click()
        campo_comentario = wait.until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH,
                 '//textarea[@placeholder="Adicione um comentário..."]')
            )
        )
        campo_comentario.send_keys(comentario)
        campo_comentario = navegador.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button/div')
        time.sleep(20)
        campo_comentario.click()
        time.sleep(20)


navegador = webdriver.Chrome()
wait = WebDriverWait(navegador, 10, 1)
executar_login()
inserir_comentario(' comentário do usuario ', 1000)
