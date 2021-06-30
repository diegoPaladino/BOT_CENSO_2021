# cadastrar_aluno


# importing libraries
import pyautogui as p
import pyperclip as pp
import tkinter as tk
import time as t



##############################################################
# root= tk.Tk()

# canvas1 = tk.Canvas(root, width = 400, height = 300)
# canvas1.pack()

# entry1 = tk.Entry (root) 
# entry2 = tk.Entry (root) 
# canvas1.create_window(200, 140, window=entry1)
# canvas1.create_window(200, 100, window=entry2)

# def teste_1():
#     x1 = entry1.get()
#     print(x1)
#     x2 = entry2.get()
#     print(x2)
    
#     label1 = tk.Label(root, text= "Memorizado!")
#     canvas1.create_window(200, 230, window=label1)
    
# button1 = tk.Button(text='memorize', command=teste_1)
# canvas1.create_window(200, 180, window=button1)

# root.mainloop()
##############################################################

sexo = p.prompt('sexo = ')




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
    p.hotkey('end')
    t.sleep(0.2)

def clicking_cadastrar_aluno():
    p.moveTo(x=310, y=-134,duration=0.2)
    p.click()
    
# def select_excel():
#     p.moveTo(x=317, y=-22,duration=0.2)
#     p.click()
#     t.sleep(0.2)
    
# def enrollment_copy():
#     p.hotkey('esc')
#     t.sleep(0.2)
#     p.hotkey('home')
#     t.sleep(0.2)
#     p.moveTo(x=260, y=180,duration=0.2)
#     p.dragTo(x=728, y=180, button='left',duration=0.2)
#     p.hotkey('ctrl','c',duration=0.2)
    
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
    
def copy_student_name_opera():
    p.moveTo(x=294, y=-464,duration=0.2)
    p.dragTo(x=648, y=-464, button='left',duration=0.2)
    p.hotkey('ctrl','c',duration=0.2)
    t.sleep(0.2)
    
def select_name_box_mozila():
    p.moveTo(x=309, y=-227,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def clicking_Dados_Familiares():
    p.moveTo(x=129, y=-285,duration=0.2)
    p.click()
    t.sleep(0.2)
    
def copy_father_name():
    p.moveTo(x=167, y=-266,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.dragTo(x=455, y=-269, button='left',duration=0.2)
    p.hotkey('ctrl','c',duration=0.2)
    t.sleep(0.2)
    
def copy_mother_name():
    p.moveTo(x=167, y=-217,duration=0.2)
    p.click()
    t.sleep(0.2)
    p.dragTo(x=456, y=-217, button='left',duration=0.2)
    p.hotkey('ctrl','c',duration=0.2)
    t.sleep(0.2)
    
def select_filiacao1():
    p.moveTo(x=304, y=-514,duration=0.2)
    p.click()
    t.sleep(0.2)
    
# def select_sexo_f():
#     p.hotkey('f')
#     t.sleep(0.2)

def sexo_sexo():
    if sexo == 'f':
        p.hotkey('f')
        t.sleep(0.2)
    else:
        p.hotkey('m')
        t.sleep(0.2)
    

def select_cor():
    p.press('p',processes=2,interval=0.025)
    t.sleep(0.2)
    
def select_nacionalidade():
    p.hotkey('b')
    t.sleep(0.2)

    
def tab_tab():
    p.hotkey('tab')
    t.sleep(0.2)
    
def copy_copy():
    p.hotkey('ctrl','c',duration=0.2)
    
def home_home():
    p.hotkey('home',duration=0.2)
    
def end_end():
    p.hotkey('end',duration=0.2)
    
def down_down():
    p.hotkey('down',duration=0.2)

    
    
# executing
select_mozila()
clicking_white_area()
positining_page()
clicking_cadastrar_aluno()

enrollment_copy()
select_opera()

copy_student_name_opera()
select_mozila()
home_home()
select_name_box_mozila()
paste_clipboard()
tab_tab()
select_opera()
tab_tab()
copy_copy()
select_mozila()
paste_clipboard() #pasting the burndate
tab_tab()
down_down()
clicking_white_area()
end_end()
select_opera()
clicking_white_area()
end_end()
clicking_Dados_Familiares()
copy_father_name()
select_mozila()
select_filiacao1()
paste_clipboard()
tab_tab()
select_opera()
copy_mother_name()
select_mozila()
paste_clipboard()
tab_tab()
# select_sexo_f()
sexo_sexo()
# tab_tab()
# select_cor()
# tab_tab()
# select_cor()
# tab_tab()
# tab_tab()


