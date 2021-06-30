# carregar dados do aluno no gemul

# importing libraries
# importing libraries
import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t


# declarations
def alert():
    p.alert('Começar pesquisa gemul')

def select_excel():
    p.moveTo(x=317, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def enrollment_copy():
    p.hotkey('esc')
    t.sleep(0.2)
    p.hotkey('home')
    t.sleep(0.2)
    p.moveTo(x=260, y=180,duration=0.2)
    p.dragTo(x=728, y=180, button='left',duration=0.2)
    p.hotkey('ctrl','c',duration=0.2)
    
def select_opera():
    p.moveTo(x=225, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)

def select_enrollment_box():
    p.moveTo(x=366, y=-524,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def paste_clipboard():
    root = tk.Tk()
    root.withdraw()
    c = root.clipboard_get()
    p.write(c,interval=0.025)
    t.sleep(0.2)
    
def scroll():
    p.scroll(-300)
    t.sleep(0.2)
    
def select_dados_familiares():
    p.moveTo(x=127, y=-130,duration=0.2)
    p.click()
    
def select_main():
    p.moveTo(x=367, y=-25,duration=0.2)
    p.click()
    p.moveTo(x=170, y=180,duration=0.2)
    p.click()
    
    
    
    
def tab_tab():
    p.hotkey('tab')
    t.sleep(0.2)
    
    
# executing
alert()
select_excel()
enrollment_copy()
select_opera()
select_enrollment_box()
paste_clipboard()
tab_tab()
t.sleep(2)
scroll()
select_dados_familiares()
select_main()
