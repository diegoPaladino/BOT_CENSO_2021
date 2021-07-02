# Main_Board_2

# importgin libraries
import os
import tkinter as tk
from tkinter import *
import tkinter.messagebox as tkmsg
from PIL import Image, ImageTk




# top = Tk()

# declarations
def ao_clicar_login():
    os.startfile("001-login_Censo_atalho")
    
def ao_clicar_pesquisa_aluno():
    os.startfile("002-pesquisa_aluno_atalho")
    
def ao_clicar_b_pesquisa_aluno():
    os.startfile("002-b-pesquisa_aluno_gemul_atalho")

def ao_clicar_reset_mozila():
    os.startfile("003-reset_mozila_censo_atalho")
    
def ao_clicar_cadastring_student():
    os.startfile("004-cadastrig_student_atalho")

def ao_clicar_b_cadastring_student():
    os.startfile("004-b-cadastrig_student_atalho")
    
def ao_clicar_vinculando_aluno():
    os.startfile("005-vinculando_aluno_atalho")
    



# root
window = Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))
# window.attributes('-fullscreen', True)
# window.geometry("1600x900+200+100")
window.title("CENSO - 2021 - diegoPaladino")

img = PhotoImage(file="main_background_4.png")
label = Label(
    window,
    image=img
)
label.place(x=0, y=0)





# Bottons
cor_botao='#01ae0d'

botao_1 = Button(window, text="Login", command=ao_clicar_login, bg=cor_botao)
botao_1.place(x=20,y=20)

botao_2 = Button(window, text="Pesquisa A", command=ao_clicar_pesquisa_aluno, bg=cor_botao)
botao_2.place(x=20,y=80)

botao_2_b = Button(window, text="Pesquisa B", command=ao_clicar_pesquisa_aluno, bg=cor_botao)
botao_2_b.place(x=110,y=80)

botao_3 = Button(window, text="Reset", command=ao_clicar_reset_mozila, bg=cor_botao)
botao_3.place(x=410,y=20)

botao_4 = Button(window, text="Cadastrar A", command=ao_clicar_cadastring_student, bg=cor_botao)
botao_4.place(x=200,y=80)

botao_4_b = Button(window, text="Cadastrar B", command=ao_clicar_cadastring_student, bg=cor_botao)
botao_4_b.place(x=300,y=80)

botao_5 = Button(window, text="Vincular", command=ao_clicar_vinculando_aluno, bg=cor_botao)
botao_5.place(x=395,y=80)


# executing
# # ABRINDO IMAGEM

###############################################################
# # root = tk.Tk()
# F1 = Frame(window)
# F1.grid(row=0)

# photo = PhotoImage(file="main_background.jpg")
# label = Label(F1, image=photo)
# label.image = photo
# label.place(x=0, y=0)

###############################################################

# # font: https://stackoverflow.com/questions/54250448/tkinter-background-image-in-frame
# IMAGE_PATH = 'main_background.jpg'
# WIDTH, HEIGHT = 250, 150

# root = tk.Tk()
# root.geometry('{}x{}'.format(WIDTH, HEIGHT))

# # Display image on a Label widget.
# img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
# lbl = tk.Label(root, image=img)
# lbl.img = img  # Keep a reference in case this code put is in a function.
# lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.

###############################################################

# font: https://stackoverflow.com/questions/15795916/image-behind-buttons-in-tkinter-photoimage

# FILENAME = 'main_background.png'
# root = tk.Tk()
# canvas = tk.Canvas(root, width=250, height=250)
# canvas.pack()
# tk_img = ImageTk.PhotoImage(file = FILENAME)
# canvas.create_image(125, 125, image=tk_img)
# quit_button = tk.Button(root, text = "Quit", command = root.quit, anchor = 'w',
#                     width = 10, activebackground = "#33B5E5")

###############################################################

# font: https://pythonguides.com/set-background-to-be-an-image-in-python-tkinter/


# img = PhotoImage(file="main_background_2.png")
# label = Label(
#     window,
#     image=img
# )
# label.place(x=0, y=0)

window.mainloop()