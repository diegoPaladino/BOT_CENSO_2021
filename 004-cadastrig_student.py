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
    
def clicking_white_area():
    p.moveTo(x=230, y=-281,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def positining_page():
    p.hotkey('home')
    t.sleep(0.2)
    p.hotkey('pagedown')
    t.sleep(0.2)

def clicking_cadastrar_aluno():
    p.moveTo(x=314, y=-236,duration=0.2)
    p.click()
    
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
    p.write(c)
    t.sleep(0.2)
    p.hotkey('tab')
    t.sleep(3)
    
def copy_student_name_opera():
    p.moveTo(x=294, y=-464,duration=0.2)
    p.dragTo(x=648, y=-464, button='left',duration=0.2)
    p.hotkey('ctrl','c',duration=0.2)
    t.sleep(0.2)
    
def select_name_box_mozila():
    p.moveTo(x=332, y=-227,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def tab_tab():
    p.hotkey('tab')
    t.sleep(0.2)
    
def copy_copy():
    p.hotkey('ctrl','c',duration=0.2)
    
def home_home():
    p.hotkey('home',duration=0.2)
    
    
# executing
select_mozila()
clicking_white_area()
positining_page()
clicking_cadastrar_aluno()
select_excel()
enrollment_copy()
select_opera()
select_enrollment_box()
paste_clipboard()
copy_student_name_opera()
select_mozila()
select_name_box_mozila(
paste_clipboard()
tab_tab()
select_opera()
tab_tab()
copy_copy()
select_mozila()
paste_clipboard()


