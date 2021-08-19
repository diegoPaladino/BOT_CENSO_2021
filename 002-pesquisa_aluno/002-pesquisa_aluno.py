# pesquisando aluno no Censo

# importing libraries
import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t


# declarations
def alert():
    p.alert('Começar pesquisa censo')

def select_excel():
    p.moveTo(x=317, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def reset_position_excel():
    p.hotkey('cls')
    t.sleep(0.2)
    
def select_student_column():
    p.hotkey('down','right')
    t.sleep(0.2)
    
def copy_student_name():
    p.moveTo(x=260, y=180,duration=0.2)
    p.dragTo(x=728, y=180, button='left',duration=0.2)
    p.hotkey('ctrl','c',duration=0.2)
    
def select_mozila():
    p.moveTo(x=271, y=-28,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def select_pesquisar_student_censo():
    p.moveTo(x=54, y=-498,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.moveTo(x=63, y=-431,duration=0.2)
    p.click()
    t.sleep(0.3)
    p.hotkey('home')
    t.sleep(1.3)
    
def paste_student_name():
    p.moveTo(x=327, y=-134,duration=0.2)
    p.click()
    p.hotkey('ctrl','a',duration=0.2)
    p.hotkey('ctrl','v',duration=0.2)
    p.hotkey('tab')
    t.sleep(0.2)
    
def select_student_burndate():
    p.hotkey('esc')
    t.sleep(0.2)
    p.press('right',presses=2,interval=0.2)
    t.sleep(0.2)
    
def paste_clipboard():
    root = tk.Tk()
    root.withdraw()
    c = root.clipboard_get()
    p.write(c,interval=0.025)
    t.sleep(0.2)
    
def enter():
    p.hotkey('enter')
    t.sleep(0.2)
    
def clicking_white_area():
    p.moveTo(x=230, y=-281,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def positining_page():
    p.hotkey('ctrl','down',duration=0.2)
    
def search_mother_name():
    p.hotkey('esc','left')
    t.sleep(0.2)
    p.moveTo(x=260, y=180,duration=0.2)
    p.dragTo(x=728, y=180, button='left',duration=0.2)
    p.hotkey('ctrl','c',duration=0.2)
    t.sleep(0.2)
    p.hotkey('esc')
    p.moveTo(x=271, y=-28,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.hotkey('ctrl','f',duration=0.2)
    t.sleep(0.2)
    p.hotkey('ctrl','v',duration=0.2)
    t.sleep(0.2)
    p.hotkey('backspace')
    t.sleep(0.2)
    
def select_main():
    p.moveTo(x=367, y=-25,duration=0.2)
    p.click()
    p.moveTo(x=170, y=180,duration=0.2)
    p.click()
    
def close_search_window():
    p.moveTo(x=1424, y=-69,duration=0.2)
    p.click()
    
def position_on_vincular():
    p.moveTo(x=300, y=-383,duration=0.2)
    
def select_visual_studio():
    p.moveTo(x=366, y=-23,duration=0.2)
    p.click()
    
def select_vs_002_b_cadastrar():
    p.moveTo(x=774, y=51,duration=0.2)
    p.click()
    
def select_play():
    p.moveTo(x=1291, y=49,duration=0.2)
    p.click()

################################
def esc_esc():
    p.hotkey('esc')
    t.sleep(0.2)
    
def enter_enter():
    p.hotkey('enter')
    t.sleep(0.2)


# execution
alert()
select_excel()
esc_esc()
reset_position_excel()
select_student_column()
copy_student_name()
select_mozila()
select_pesquisar_student_censo()
paste_student_name()
select_excel()
select_student_burndate()
copy_student_name()
select_mozila()
paste_clipboard()
t.sleep(1)
enter()
clicking_white_area()
positining_page()
select_excel()
search_mother_name()
enter()
close_search_window()
select_visual_studio()
select_vs_002_b_cadastrar()
select_play()
t.sleep(0.2)
# select_main()
# position_on_vincular()