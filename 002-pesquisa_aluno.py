# pesquisando aluno no Censo

# importing libraries
import pyautogui as p
import pyperclip as pp
import time as t


# declarations
def select_excel():
    p.moveTo(x=317, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.keyDown('ctrl')
    p.hotkey('home')
    p.keyUp('ctrl')
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
    t.sleep(1)
    p.moveTo(x=327, y=-134,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.hotkey('ctrl','v',duration=0.2)
    p.hotkey('tab')
    
def select_student_burndate():
    p.hotkey('esc')
    t.sleep(0.2)
    
    


# execution
select_excel()
select_student_column()
copy_student_name()
select_mozila()
select_pesquisar_student_censo()
select_excel()



