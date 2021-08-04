# 005-vinculando_aluno


# importing libraries
import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t

# declarations
def alert():
    p.alert('Começar vincular?')
    
def clicking_white_area():
    p.moveTo(x=230, y=-281,duration=0.2)
    p.click()
    t.sleep(0.2)

def click_vinculando_aluno():
    p.moveTo(x=301, y=-504,duration=0.2)
    p.click()
    t.sleep(0.3)

    
def select_class_box():
    p.moveTo(x=339, y=-321,duration=0.2)
    p.click()
    t.sleep(0.5)

def select_class():
    p.press('down',presses=16)#                               <<<<<<<<<<<<<< CLASS SELECTION
    t.sleep(0.2)
    p.hotkey('tab')
    t.sleep(0.2)
    
def end_end():
    p.hotkey('end')
    t.sleep(0.2)

def home_home():
    p.hotkey('home')
    t.sleep(0.2)
    
def esc_esc():
    p.hotkey('esc')
    t.sleep(0.2)
    
def up_up():
    p.hotkey('up')
    t.sleep(0.2)

def select_24_box():
    p.moveTo(x=358, y=-334,duration=0.2)
    p.click()
    t.sleep(0.3)
    
    
def select_25_check_box():
    p.moveTo(x=264, y=-231,duration=0.2)
    p.click()
    t.sleep(0.2)

def enviar():
    p.moveTo(x=1291, y=-131,duration=0.2)
    p.click()
    t.sleep(2)
    
# def select_main():
#     p.moveTo(x=367, y=-25,duration=0.2)
#     p.click()
#     p.moveTo(x=170, y=180,duration=0.2)
#     p.click()
    
def select_excel():
    p.moveTo(x=317, y=-22,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def status_ok():
    p.press('right',presses=11,interval=0.025)
    p.typewrite('OK')
    t.sleep(0.2)
    p.hotkey('enter')
    t.sleep(0.2)
    p.hotkey('up')
    t.sleep(0.2)
    
def select_main():
    p.moveTo(x=367, y=-25,duration=0.2)
    p.click()
    p.moveTo(x=63, y=120,duration=0.2)
    p.click()

def select_mozila():
    p.moveTo(x=271, y=-28,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def reset_itemns():
    p.moveTo(x=203, y=-727,duration=0.2)
    p.click()
    t.sleep(0.5)
    p.moveTo(x=203, y=-727,duration=0.2)
    p.click()


    
# execution
alert()
# clicking_white_area()
# end_end()
# click_vinculando_aluno()
select_class_box()
select_class()
clicking_white_area()
end_end()
select_25_check_box()
enviar()
select_excel()
esc_esc()
home_home()
status_ok()
select_mozila()
reset_itemns()
select_main()
