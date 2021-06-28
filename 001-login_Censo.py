# 
# link of repository: https://pt.stackoverflow.com/questions/147660/fatal-not-a-git-repository


import winsound as ws
import tkinter as tk
import pyautogui as p
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
cont = 0
total = 2



#functions
def select_excel():
    p.moveTo(246,-25)
    p.click()
    time.sleep(0.2)

def select_mozila():
    p.moveTo(194, -23)
    p.click()
    time.sleep(0.3)

def copy():
    p.hotkey('ctrl','c')
    time.sleep(0.3)

def paste():
    p.hotkey('ctrl','v')
    time.sleep(0.3)

#buscando o executável do drive do Firefox
operadriver='C://Users//Diego//Desktop//DESKTOP//PROGRAMAS//WEB-DRIVERS//OPERADRIVER-2//geckodriver.exe'
driver = webdriver.Firefox()
#solicitando a abertura da página do censo
driver.get('http://censobasico.inep.gov.br/censobasico/#/')
driver.set_window_position(166,-700)
driver.maximize_window()

#efetuando o login na página inicial
username = driver.find_element_by_id('login')
password = driver.find_element_by_id('input_senha')
username.send_keys('02124377124')
password.send_keys('P@ladino804680')

#nesse instante aguarda-se para a selelção manual(ainda não sesenvolvida solução IA para reconhecimento automático de objetos capchta)

#tentativa de abertura da pesquisa do aluno >> deu certo!!
time.sleep(8)
driver.find_element_by_xpath('/html/body/div[5]/div/div/aside[1]/div/section/ul[2]/li[5]/a/span').click()
driver.find_element_by_xpath('/html/body/div[5]/div/div/aside[1]/div/section/ul[2]/li[5]/ul/li[3]/a/span').click()

time.sleep(1.5)