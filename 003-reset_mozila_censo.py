# reset_mozila_censo


# importing libraries
import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t

# declarating

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
    
    
def click_aluno():
    p.moveTo(x=21, y=-497,duration=0.2)
    p.click()
    
def mouse_reposition_1():
    p.moveTo(x=589, y=48,duration=0.2)
    
def select_opera():
    p.moveTo(x=225, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def select_first_window():
    p.moveTo(x=108, y=-888,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def refresh_enrollment():
    p.moveTo(x=247, y=-681,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.moveTo(x=243, y=-558,duration=0.2)
    p.click()
    t.sleep(0.2)

# executing

select_mozila()
select_link_bar()
paste_link()
click_aluno()
select_opera()
select_first_window()
refresh_enrollment()
# mouse_reposition_1()
