# cadastro de CPF e CEP do aluno no Censo 2021

import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t

# declarations
def alert():
    p.alert('Começar CPF?')
    
def select_opera():
    p.moveTo(x=225, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def copy_CPF_box():
    p.moveTo(x=294, y=-785,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.dragTo(x=387, y=-784, button='left',duration=0.5)
    p.hotkey('ctrl','c',duration=0.2)
    
def select_mozila():
    p.moveTo(x=271, y=-28,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def select_Mozila_CPF_box():
    p.moveTo(x=283, y=-348,duration=0.2)
    p.click()
    
def enviar():
    p.moveTo(x=1282, y=-112,duration=0.2)
    p.click()
    
#####################################
def home_home():
    p.hotkey('esc')
    p.hotkey('home')
    t.sleep(0.2)

def write_write():
    root = tk.Tk()
    root.withdraw()
    c = root.clipboard_get()
    p.write(c,interval=0.025)
    t.sleep(0.2)
    
def pagedown_pagedown():
    p.hotkey('pagedown')
    t.sleep(0.2)

    
##################################

    
# code execution
select_opera()
copy_CPF_box()
select_mozila()
select_Mozila_CPF_box()
write_write()
pagedown_pagedown()
enviar()
