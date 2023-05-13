from typing import List
import tkinter as tk
from deck import Deck
import TkAddCard
import TkStudyCard
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

    #lista que ocupada 50% de la ventana centra
    listbox = tk.Listbox(ventana,font=("Arial", 16))
    listbox.pack(side=tk.LEFT, padx=40, pady=10)
    i=1
    for mazo in mazos:
        i=i+1
        listbox.insert(i,mazo.name)
    
    def nuevo_mazo():
        listbox.insert(listbox.size(),entry_box.get())
        listbox.config(height=listbox.size())
        mazos.append(Deck(entry_box.get()))
        borrar_textos()

    def borrar_mazo():
        selection = listbox.curselection()
        if selection:
            index = selection[0]
            mazo_name = listbox.get(index)
            listbox.delete(index)
            listbox.config(height=listbox.size())
            for i, mazo in enumerate(mazos):
                if mazo.name == mazo_name:
                    mazos.pop(i)
                    break


    def anadir_cartas():
        for mazo in mazos:
            if mazo.name==listbox.get(listbox.curselection()):
                TkAddCard.exec(mazo)

    def study():
        for mazo in mazos:
            if mazo.name==listbox.get(listbox.curselection()):
                TkStudyCard.exec(mazo)

    listbox.config(height=listbox.size())

    #crear marco para meter btotones de añadir carta, borrar mazo
    marco_botones = tk.Frame(ventana)
    marco_addDeck = tk.Frame(ventana)
    marco_botones.pack(side=tk.TOP, padx=40, pady=60)
    marco_addDeck.pack(side=tk.BOTTOM, padx=40, pady=30)

    crear_button = tk.Button(marco_addDeck,text="Añadir mazo",command=nuevo_mazo,font=("Arial", 16))
    crear_button.pack(side=tk.BOTTOM, padx=40, pady=10)

    entry_box=tk.Entry(marco_addDeck,font=("Arial", 16))
    entry_box.pack(side=tk.BOTTOM, padx=40)

    crear_button = tk.Button(marco_botones,text="Borrar",command=borrar_mazo,font=("Arial", 16))
    crear_button.pack()

    crear_button = tk.Button(marco_botones,text="Study",command=study,font=("Arial", 16))
    crear_button.pack()

    crear_button = tk.Button(marco_botones,text="Añadir cartas",command=anadir_cartas, font=("Arial", 16))
    crear_button.pack()

    def borrar_textos():
        entry_box.delete(0, tk.END)


    

    ventana.mainloop()