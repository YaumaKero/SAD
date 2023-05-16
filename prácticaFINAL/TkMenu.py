from typing import List
import tkinter as tk
from deck import Deck
import TkAddCard
import TkStudyCard

def exec(mazos:List[Deck]):
    # Crear la ventana principal
    ventana = tk.Tk()

    # Obtener el ancho y la altura de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()
    # Calcular las coordenadas para centrar la ventana
    x = (ancho_pantalla - 700) // 2 # El ancho de la ventana es 300
    y = (altura_pantalla - 400) // 2 # La altura de la ventana es 300
    # Establecer la posición de la ventana en el centro de la pantalla
    ventana.geometry(f"700x400+{x}+{y}")
    ventana.title("Flashcard Study Manager with AI")

    # Crear y colocar lista de mazos
    listbox = tk.Listbox(ventana,font=("Arial", 16))
    listbox.pack(side=tk.LEFT, padx=40, pady=10)
    listbox.config(height=listbox.size())

    # Relleno la listas con los mazos existentes
    i=1
    for mazo in mazos:
        i=i+1
        listbox.insert(i,mazo.name)
    
    # Defino comandos para crear nuevo mazo
    def nuevo_mazo():
        listbox.insert(listbox.size(),entry_box.get())
        listbox.config(height=listbox.size())
        mazos.append(Deck(entry_box.get()))
        entry_box.delete(0, tk.END)
    # Defino comandos para borrar mazo
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
    # Defino comandos para añadir tarjetas a un mazo existente
    def anadir_cartas():
        for mazo in mazos:
            if mazo.name==listbox.get(listbox.curselection()):
                TkAddCard.exec(mazo)
    # Defino comandos para abrir la ventana de estudio de tarjetas de un mazo
    def study():
        for mazo in mazos:
            if mazo.name==listbox.get(listbox.curselection()):
                TkStudyCard.exec(mazo)


    # Crear marco para botones de añadir carta, borrar mazo y estudiar
    marco_botones = tk.Frame(ventana)
    marco_addDeck = tk.Frame(ventana)
    marco_botones.pack(side=tk.TOP, padx=40, pady=60)
    marco_addDeck.pack(side=tk.BOTTOM, padx=40, pady=30)
    # Creo botones y entradas de texto
    crear_button = tk.Button(marco_addDeck,text="Add Deck",command=nuevo_mazo,font=("Arial", 16))
    crear_button.pack(side=tk.BOTTOM, padx=40, pady=10)

    entry_box=tk.Entry(marco_addDeck,font=("Arial", 16))
    entry_box.pack(side=tk.BOTTOM, padx=40)

    crear_button = tk.Button(marco_botones,text="Delete",command=borrar_mazo,font=("Arial", 16))
    crear_button.pack()

    crear_button = tk.Button(marco_botones,text="Study",command=study,font=("Arial", 16))
    crear_button.pack()

    crear_button = tk.Button(marco_botones,text="Add Cards",command=anadir_cartas, font=("Arial", 16))
    crear_button.pack()

    # Iniciar el ciclo principal de eventos
    ventana.mainloop()