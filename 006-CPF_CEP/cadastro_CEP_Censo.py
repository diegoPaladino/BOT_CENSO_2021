
import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t

# declarations
def alert():
    p.alert('Começar CEP?')
    
def select_opera():
    p.moveTo(x=225, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def copy_CEP_box():
    p.moveTo(x=143, y=-250,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.dragTo(x=216, y=-250, button='left',duration=0.5)
    p.hotkey('ctrl','c',duration=0.2)
    
def select_mozila():
    p.moveTo(x=271, y=-28,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def select_Mozila_CEP_box():
    p.moveTo(x=285, y=-128,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.dragTo(x=360, y=-128,button='left',duration=0.5)
    
def write_CEP():
    root = tk.Tk()
    root.withdraw()
    c = root.clipboard_get()
    p.write(c,interval=0.025)
    t.sleep(0.2)
    
def enviar_CEP():
    p.moveTo(x=1295, y=-170,duration=0.2)
    p.click()
    
    
################################

def backspace_backspace():
    p.hotkey('backspace')
    p.sleep(0.2)

def down_down():
    p.hotkey('pagedown')
    p.sleep(0.2)

def clicking_white_area():
    p.moveTo(x=230, y=-281,duration=0.2)
    p.click()
    t.sleep(0.2)

    
#################################
alert()
select_opera()
copy_CEP_box()
select_mozila()
select_Mozila_CEP_box()
backspace_backspace()
write_CEP()
clicking_white_area()
down_down()
enviar_CEP()



