import tkinter as tk
from tkinter import ttk
import time
import threading


main_window = tk.Tk()
main_window.title("Ejemplo")
main_window.configure(width=400, height=200)

def opcionFinal():
    boton = ttk.Button(main_window, text="Salir", command=main_window.destroy)
    boton.place(x=170, y=170)

def createLabel(a,b):
    label = ttk.Label(text="")
    label.place(x=a,y=b)
    return label

def crearAnimacion(a, b, char):
    mylabel = createLabel(a=a,b=b)
    texto=""
    retardo: float=0.45
    for i in range(0,35):
        time.sleep(retardo)
        texto += char
        mylabel.config(text = texto)
        main_window.update()

t1 = threading.Thread(target= crearAnimacion, args=(0, 10, 'X'))
t2 = threading.Thread(target= crearAnimacion, args=(0, 30, 'Y'))
t3 = threading.Thread(target= crearAnimacion, args=(0, 50, 'Z'))

t1.start()
t2.start()
t3.start()

opcionFinal()
main_window.mainloop()
