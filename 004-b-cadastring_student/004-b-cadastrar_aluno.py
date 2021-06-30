# 004-b-cadastrar_aluno


# importing libraries
import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t

# declarations
def select_opera():
    p.moveTo(x=225, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)

def copy_num_cert_nasc():
    p.moveTo(x=293, y=-404,duration=0.2)
    p.dragTo(x=585, y=-405, button='left',duration=0.6)
    p.hotkey('ctrl','c',duration=0.2)
    t.sleep(0.2)
    
def select_mozila():
    p.moveTo(x=271, y=-28,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def select_num_cert_nasc_box():
    p.moveTo(x=288, y=-387,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def paste_clipboard():
    root = tk.Tk()
    root.withdraw()
    c = root.clipboard_get()
    p.write(c,interval=0.025)
    t.sleep(0.2)
    
def click_endereco():
    p.moveTo(x=98, y=-429,duration=0.2)
    p.click()
    t.sleep(0.2)

def copy_cep():
    p.moveTo(x=143, y=-411,duration=0.2)
    p.dragTo(x=220, y=-411, button='left',duration=0.6)
    p.hotkey('ctrl','c',duration=0.2)
    t.sleep(0.2)

def urbana():
    p.hotkey('u')
    t.sleep(0.2)
    
def localizacao():
    p.hotkey('n')
    t.sleep(0.2)
    
    

    
def esc_esc():
    p.hotkey('esc')
    t.sleep(0.2)

def home_home():
    p.hotkey('home')
    t.sleep(0.2)

def tab_tab():
    p.hotkey('tab')
    t.sleep(0.2)
    
def down_down():
    p.hotkey('down')
    t.sleep(0.2)



# execution
select_opera()
esc_esc()
home_home()
copy_num_cert_nasc()
select_mozila()
select_num_cert_nasc_box()
paste_clipboard()
tab_tab()
tab_tab
select_opera()
down_down()
click_endereco()
copy_cep()
select_mozila()
paste_clipboard()
tab_tab()
tab_tab()
tab_tab()
urbana()
localizacao()

