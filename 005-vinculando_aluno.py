# 005-vinculando_aluno


# importing libraries
import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t

# declarations
def click_vinculando_aluno():
    p.moveTo(x=297, y=-322,duration=0.2)
    p.click()
    t.sleep(0.5)
            
def select_class_box():
    p.moveTo(x=339, y=-321,duration=0.2)
    p.click()
    t.sleep(0.5)

def select_class():
    p.hotkey('down')
    t.sleep(0.2)
    

# execution