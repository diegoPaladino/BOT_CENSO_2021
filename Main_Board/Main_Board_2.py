# Main_Board_2

# importgin libraries
import os
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkmsg
from PIL import Image, ImageTk

top = Tk()

# declarations
def ao_clicar_login():
    os.startfile("001-login_Censo_atalho")
    
def ao_clicar_pesquisa_aluno():
    os.startfile("002-pesquisa_aluno_atalho")

def ao_clicar_reset_mozila():
    os.startfile("003-reset_mozila_censo_atalho")
    
def ao_clicar_cadastring_student():
    os.startfile("004-cadastrig_student_atalho")
    
def ao_clicar_vinculando_aluno():
    os.startfile("005-vinculando_aluno_atalho")
    



# root
window = Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
# window.attributes('-fullscreen', True)
# window.geometry("1600x900+200+100")
window.title("CENSO - 2021 - diegoPaladino")




# Bottons

botao_1 = Button(window, text="Login", command=ao_clicar_login, bg='SeaGreen2')
botao_1.place(x=40,y=50)

botao_2 = Button(window, text="Pesquisa", command=ao_clicar_pesquisa_aluno, bg='SeaGreen2')
botao_2.place(x=100,y=50)

botao_3 = Button(window, text="Reset", command=ao_clicar_reset_mozila, bg='SeaGreen2')
botao_3.place(x=180,y=50)

botao_4 = Button(window, text="Cadastrar", command=ao_clicar_cadastring_student, bg='SeaGreen2')
botao_4.place(x=240,y=50)

botao_5 = Button(window, text="Vincular", command=ao_clicar_vinculando_aluno, bg='SeaGreen2')
botao_5.place(x=320,y=50)



# #################################

def ao_clicar_sbmitbtn():
    print(name)

name = Label(top, text = "Name").place(x = 30,y = 50)  
  
email = Label(top, text = "Email").place(x = 30, y = 90)  
  
password = Label(top, text = "Password").place(x = 30, y = 130)  
  
sbmitbtn = Button(top, text = "Submit",activebackground = "pink", activeforeground = "blue", command=ao_clicar_sbmitbtn).place(x = 30, y = 170)  
  
e1 = Entry(top).place(x = 80, y = 50)  
  
  
e2 = Entry(top).place(x = 80, y = 90)  
  
  
e3 = Entry(top).place(x = 95, y = 130)  
  
top.mainloop()
# executing

window.mainloop()