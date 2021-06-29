# Main_Board_2

# importgin libraries
import os
import tkinter
from tkinter import *
import tkinter.messagebox as tkmsg
from PIL import Image, ImageTk

# declarations
def ao_clicar_login():
    os.startfile("001-login_Censo_atalho")
    
def ao_clicar_pesquisa_aluno():
    os.startfile("002-pesquisa_aluno_atalho")

def ao_clicar_reset_mozila():
    os.startfile("003-reset_mozila_censo_atalho")
    
def ao_clicar_cadastring_student():
    os.startfile("")
    
def ao_clicar_vinculando_aluno():
    os.startfile("")
    



# root
window = Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
# window.attributes('-fullscreen', True)
# window.geometry("1600x900+200+100")
window.title("CENSO - 2021 - diegoPaladino")




# Bottons

botao_1 = Button(window, text="Login", command=ao_clicar_login, bg='SeaGreen2')
botao_1.place(x=50,y=50)

botao_2 = Button(window, text="Pesquisa", command=ao_clicar_pesquisa_aluno, bg='SeaGreen2')
botao_2.place(x=100,y=50)

botao_3 = Button(window, text="Reset", command=ao_clicar_reset_mozila, bg='SeaGreen2')
botao_3.place(x=180,y=50)
# executing

window.mainloop()