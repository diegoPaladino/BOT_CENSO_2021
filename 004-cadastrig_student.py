# cadastrar_aluno





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
    p.write('http://censobasico.inep.gov.br/censobasico/#/aluno/cadastrar')
    p.hotkey('enter')
    t.sleep(0.5)
    
def respositioning_home_page():
    p.hotkey('home')
    t.sleep(0.2)
    
def select_excel():
    p.moveTo(x=317, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def enrollment_copy():
    p.hotkey('esc')
    t.sleep(0.2)
    p.hotkey('home')
    t.sleep(0.2)
    
def copy_student_enrollment():
    p.moveTo(x=260, y=180,duration=0.2)
    p.dragTo(x=728, y=180, button='left',duration=0.2)
    p.hotkey('ctrl','c',duration=0.2)
    
    
def select_opera():
    p.moveTo(x=225, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)
    
# executing
select_mozila()
select_link_bar()
paste_link()
respositioning_home_page()
select_excel()
select_opera()