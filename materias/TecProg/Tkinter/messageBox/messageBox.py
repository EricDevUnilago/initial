from tkinter import *
from tkinter import messagebox

window = Tk()

window.geometry("800X800")

def click():
    messagebox.showinfo("Dialogo de teste", "Este diálogo é para teste de informação")

btn = Button(window, text="teste", command=click)

window.mainloop()