# 005-vinculando_aluno


# importing libraries
import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()

# declarations
def click_vinculando_aluno():
    p.moveTo(x=300, y=-365,duration=0.2)
    p.click()
    t.sleep(0.5)
    
def clicking_white_area():
    p.moveTo(x=230, y=-281,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def click_vinculando_aluno_2():
    driver.find_element_by_link_text("Vincular").click()
            
def select_class_box():
    p.moveTo(x=339, y=-321,duration=0.2)
    p.click()
    t.sleep(1)

def select_class():
    p.press('down',presses=1)#           <<<<<<<<<<<<<<<<<<<<<<<<< Class adjust
    t.sleep(0.2)
    
def down_down():
    p.hotkey('end')
    t.sleep(0.2)

def home_home():
    p.hotkey('home')
    t.sleep(0.2)

def select_24_box():
    p.moveTo(x=358, y=-334,duration=0.2)
    p.click()
    t.sleep(0.3)
    
    
def select_25_check_box():
    p.moveTo(x=263, y=-2324,duration=0.2)
    p.click()
    t.sleep(0.2)

def enviar():
    p.moveTo(x=1291, y=-131,duration=0.2)
    p.click()
    t.sleep(2)
    
def select_main():
    p.moveTo(x=367, y=-25,duration=0.2)
    p.click()
    p.moveTo(x=170, y=180,duration=0.2)
    p.click()
    
def select_excel():
    p.moveTo(x=317, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def status_ok():
    p.press('right',presses=11,interval=0.025)
    p.typewrite('OK')
    t.sleep(0.2)
    p.hotkey('enter')
    t.sleep(0.2)

# execution
# click_vinculando_aluno()
clicking_white_area()
click_vinculando_aluno_2()
select_class_box()
select_class()
down_down()
select_25_check_box()
enviar()
select_excel()
home_home()
status_ok()
select_main()
