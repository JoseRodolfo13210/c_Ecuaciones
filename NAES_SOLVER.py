'''    CREACION DE INTERFAZ PARA INGRESAR DATOS EN CUADROS DE TEXTO CON BARRA DE DESPLAZAMIENTO    '''

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

#Creacion de mi funcion
def resultado():
    res.insert(tk.INSERT, "Creacion de una interfaz de usuario donde el boton tiene la funcion de imprimir en un cuadro de texto el def del codigo.   ")

window = tk.Tk()

window.title('NAES Solver')
window.geometry('650x450')

#Entrada en horizontal 
ttk.Label(window, text = "Variables"). grid(column=0, row=0)
src = scrolledtext.ScrolledText(window, width = 20, height = 2, wrap = tk.WORD)
src.grid(column = 7, row = 1)

#Entrada en horizontal y vertical
ttk.Label(window, text = "Ecuaciones"). grid(column = 0, row = 5)
src = scrolledtext.ScrolledText(window, width = 20, height = 5, wrap = tk.WORD)
src.grid(column = 7, row = 7)


#Creacion del cuadro de texto para imprimir la funcion
res = scrolledtext.ScrolledText(window, width = 25, height = 7, wrap = tk.WORD)
res.grid(column = 20, row = 7)

#Creacion del boton para imprimir la funcion
action=ttk.Button(window, text="Picale", command=resultado).grid(column=8, row=4)

window.mainloop()


