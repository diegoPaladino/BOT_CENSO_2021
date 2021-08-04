# reset_mozila_censo


# importing libraries
import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t

# declarating
def alert():
    p.alert('Começar reset?')

def select_mozila():
    p.moveTo(x=271, y=-28,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def select_link_bar():
    p.moveTo(x=402, y=-835,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.hotkey('ctrl','a')
    t.sleep(0.2)

def paste_link():
    p.write('http://censobasico.inep.gov.br/censobasico/#/inicioMatricula')
    p.hotkey('enter')
    t.sleep(0.5)
    
    
def reset_itemns():
    p.moveTo(x=203, y=-727,duration=0.2)
    p.click()
    t.sleep(0.5)
    p.moveTo(x=203, y=-727,duration=0.2)
    p.click()
    
    
def mouse_reposition_1():
    p.moveTo(x=369, y=-25,duration=0.2)
    p.click()
    
def select_opera():
    p.moveTo(x=225, y=-22,duration=0.2)
    p.click()
    t.sleep(0.3)
    
def select_first_opera_window():
    p.moveTo(x=125, y=-885,duration=0.2)
    p.click()
    t.sleep(0.3)
    
def select_first_window():
    p.moveTo(x=108, y=-888,duration=0.2)
    p.click()
    t.sleep(0.3)
    
def refresh_enrollment():
    p.moveTo(x=254, y=-709,duration=0.2)
    p.click()
    t.sleep(0.3)
    p.moveTo(x=245, y=-582,duration=0.2)
    p.click()
    t.sleep(0.3)
    
def home_home():
    p.hotkey('home')
    t.sleep(0.3)
    
def esc_esc():
    p.hotkey('esc')
    t.sleep(0.3)

# executing
alert()
select_mozila()
select_link_bar()
paste_link()
reset_itemns()
select_opera()
select_first_opera_window()
esc_esc()
home_home()
refresh_enrollment()
mouse_reposition_1()
