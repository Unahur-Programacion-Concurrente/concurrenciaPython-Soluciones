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

class Animacion(threading.Thread):
    a = 0
    b = 0
    char = ""

    def __init__(self, a, b, char):
        super().__init__()
        self.a = a
        self.b = b
        self.char = char

    def run(self):
        texto = ""
        label = ttk.Label(text="")
        label.place(x=self.a, y=self.b)
        print(str(self.a) + str(self.b) + self.char)
        retardo: float=0.45
        for i in range(0,35):
            time.sleep(retardo)
            texto += self.char
            label.config(text = texto)
            main_window.update()

t1 = Animacion(0, 10, 'X')
t2 = Animacion(0, 30, 'Y')
t3 = Animacion(0, 50, 'Z')

t1.start()
t2.start()
t3.start()

opcionFinal()
main_window.mainloop()
