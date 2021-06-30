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
    
def esc_esc():
    p.hotkey('esc')
    t.sleep(0.2)

def home_home():
    p.hotkey('home')
    t.sleep(0.2)




# execution
select_opera()
esc_esc()
home_home()
copy_num_cert_nasc()

