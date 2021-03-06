import sys
from tkinter import *

def salir():
    login_frame.destroy()
    home_frame = home()
    home_frame.pack(fill="both", expand=True)

def home():
    frame = Frame(root)
    Label(frame, text="Welcome").pack()
    return frame

def login():
    frame = Frame(root)
    Label(frame, text="Bienvenido a Matricula UTEC").grid(row=0)
    Label(frame, text="Ingrese sus nombres: ").grid(row=1)
    Label(frame, text="Ingrese sus apellidos: ").grid(row=2)
    e1 = Entry(frame)
    e2 = Entry(frame)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    Button(frame, text='Salir', command=salir).grid(
        row=4, column=0, sticky=W, pady=4)
    Button(frame, text='Comenzar', command=salir).grid(
        row=4, column=1, sticky=W, pady=4)
    return frame

def home():
    frame = Frame(root)
    Label(frame, text="Welcome").pack()
    return frame


root = Tk()
root.wm_title('Matricula UTEC')

login_frame = login()
login_frame.pack(fill="both", expand=True)

root.mainloop()
