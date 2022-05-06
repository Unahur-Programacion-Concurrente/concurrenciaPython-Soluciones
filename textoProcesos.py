import tkinter as tk
from tkinter import ttk
import time
import multiprocessing


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
    print("Este es el proceso %d"%multiprocessing.current_process().pid)
    mylabel = createLabel(a=a,b=b)
    texto=""
    retardo: float=0.25
    for i in range(0,35):
        time.sleep(retardo)
        texto += char
        mylabel.config(text = texto)
        main_window.update()

if __name__ == '__main__':

    t1 = multiprocessing.Process(target= crearAnimacion, args=(0, 10, 'X'))
    t2 = multiprocessing.Process(target= crearAnimacion, args=(0, 30, 'Y'))
    t3 = multiprocessing.Process(target= crearAnimacion, args=(0, 50, 'Z'))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

 #   opcionFinal()
    main_window.mainloop()
