import tkinter as tk

#ventana con 4 columnas, la primera el nombre del mazo, la segunda tercera y cuarta botones de añadir carta, estudiar y eliminar mazo

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

#crear marco general
marco_general = tk.Frame(ventana)
marco_general.pack(pady=10)

#crear marco para nombre y los 3 botones asociados a ese mazo
marco_filas = tk.Frame(marco_general)
marco_filas.pack(pady=10)

mazos = ["Mazo 1", "Mazo 2"]
marcos_filas = []
botones_eliminar = [] # Lista para almacenar los botones de eliminación de cada mazo


#bucle que cree tantas filas como mazos haya
for i, mazo in enumerate(mazos):    #crear marco para cada fila
    marco_filas = tk.Frame(marco_general)
    marco_filas.pack(pady=10)
    marcos_filas.append(marco_filas)
    #crear el texto del nombre del mazo
    texto1 = tk.Label(marco_filas, text=mazos[i], font=("Arial", 16))
    texto1.pack(side=tk.LEFT, padx=30) # Ajustar el espacio entre widgets
    #crear los 3 botones asociados al primer mazo uno detras dedl otro horizontalmente
    boton1 = tk.Button(marco_filas, text="Add card", font=("Arial", 16))
    boton1.pack(side=tk.LEFT, padx=10) # Ajustar el espacio entre widgets
    boton2 = tk.Button(marco_filas, text="Study", font=("Arial", 16))
    boton2.pack(side=tk.LEFT, padx=10) # Ajustar el espacio entre widgets
    boton3 = tk.Button(marco_filas, text="X", font=("Arial", 16))
    boton3.pack(side=tk.LEFT, padx=10) # Ajustar el espacio entre widgets
    botones_eliminar.append(boton3)


#crear boton para añadir mazo justo debajo de los nombres de los mazos
boton4 = tk.Button(marco_general, text="Add deck", font=("Arial", 16))
boton4.pack(side=tk.BOTTOM, anchor=tk.SW, padx=10, pady=10) # Ajustar el espacio entre widgets

def añadirMazoaLista(event): 
    i = len(mazos)   
    #cuadro de texto para añadir el nombre del mazo
    texto1 = tk.Label(marco_general, text="Nombre del mazo: ", font=("Arial", 16))   
    mazos.append("mazo "+str(i+1))
    # crear un nuevo marco para el mazo añadido
    nuevo_marco = tk.Frame(marco_general)
    nuevo_marco.pack(pady=10)
    marcos_filas.append(nuevo_marco)
    # crear los widgets para el nuevo mazo
    texto1 = tk.Label(nuevo_marco, text=mazos[-1], font=("Arial", 16))
    texto1.pack(side=tk.LEFT, padx=30)
    boton1 = tk.Button(nuevo_marco, text="Add card", font=("Arial", 16))
    boton1.pack(side=tk.LEFT, padx=10)
    boton2 = tk.Button(nuevo_marco, text="Study", font=("Arial", 16))
    boton2.pack(side=tk.LEFT, padx=10)
    boton3 = tk.Button(nuevo_marco, text="X", font=("Arial", 16))
    boton3.pack(side=tk.LEFT, padx=10)
    botones_eliminar.append(boton3)
    boton_eliminar = nuevo_marco.children['!button3']
    boton_eliminar.bind("<Button-1>", eliminarWidget)
    ventana.update()
boton4.bind("<Button-1>", añadirMazoaLista)

# Vincular la función eliminarWidget al evento del botón de eliminación de todos los mazos
def eliminarWidget(event):
    # Obtener el índice del marco que contiene el botón de eliminación que fue presionado
    index = marcos_filas.index(event.widget.master)
    # Eliminar el marco del mazo completo
    marcos_filas[index].destroy()
    # Eliminar el mazo de la lista de mazos
    del mazos[index]
    event.widget.master.destroy()
for marco in marcos_filas:
    boton_eliminar = marco.children['!button3'] # Obtener el botón de eliminación del mazo
    boton_eliminar.bind("<Button-1>", eliminarWidget)



























# Iniciar el ciclo principal de eventos
ventana.mainloop()

