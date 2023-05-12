from typing import List
import tkinter as tk
from deck import Deck
import addCardGUI
#ventana con 4 columnas, la primera el nombre del mazo, la segunda tercera y cuarta botones de añadir carta, estudiar y eliminar mazo

def exec(mazos:List[Deck]):
    # Crear la ventana principal
    ventana = tk.Tk()

    # Obtener el ancho y la altura de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    x = (ancho_pantalla - 300) // 2 # El ancho de la ventana es 300
    y = (altura_pantalla - 300) // 2 # La altura de la ventana es 300

    # Establecer la posición de la ventana en el centro de la pantalla
    ventana.geometry(f"600x400+{x}+{y}")
    ventana.title("App Flashcards")

    listbox = tk.Listbox(ventana)
    listbox.pack()
    i=1
    for mazo in mazos:
        i=i+1
        listbox.insert(i,mazo.name)
    
    def nuevo_mazo():
        listbox.insert(listbox.size(),entry_box.get())
        listbox.config(height=listbox.size())
        mazos.append(Deck(entry_box.get()))

    def borrar_mazo():
        listbox.delete(listbox.curselection())
        listbox.config(height=listbox.size())
        for mazo in mazos:
            if mazo.name==listbox.get(listbox.curselection()):
                mazos.remove(mazo)

    def anadir_cartas():
        for mazo in mazos:
            if mazo.name==listbox.get(listbox.curselection()):
                addCardGUI.exec(mazo)

    listbox.config(height=listbox.size())

    crear_button = tk.Button(ventana,text="Añadir mazo",command=nuevo_mazo)
    crear_button.pack()

    crear_button = tk.Button(ventana,text="Borrar",command=borrar_mazo)
    crear_button.pack()

    crear_button = tk.Button(ventana,text="Añadir cartas",command=anadir_cartas)
    crear_button.pack()

    entry_box=tk.Entry(ventana)
    entry_box.pack()

    ventana.mainloop()
