

import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Obtener el ancho y la altura de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
altura_pantalla = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla - 300) // 2 # El ancho de la ventana es 300
y = (altura_pantalla - 300) // 2 # La altura de la ventana es 300

# Establecer la posición de la ventana en el centro de la pantalla
ventana.geometry(f"500x300+{x}+{y}")
ventana.title("App Flashcards")

# Crear el marco para los textos
marco_textos = tk.Frame(ventana)
marco_textos.pack(pady=40)

# Crear los campos de entrada de texto
texto1 = tk.Entry(marco_textos, font=("Arial", 16), fg='grey', bg='white')
texto1.insert(0, "Front of the card")
texto1.pack(pady=10) # Ajustar el espacio entre widgets
texto2 = tk.Entry(marco_textos, font=("Arial", 16), fg='grey', bg='white')
texto2.insert(0, "Back of the card")
texto2.pack(pady=10) # Ajustar el espacio entre widgets

# Función para borrar el texto de fondo al hacer clic
def borrar_texto1(event):  
     
    if texto1.get() == "Front of the card":
        texto1.delete(0, "end")
        texto1.config(fg='black')
def borrar_texto2(event):       
    if texto2.get() == "Back of the card":
        texto2.delete(0, "end")
        texto2.config(fg='black')
# Asociar la función con el evento clic en el Entry
texto1.bind("<Button-1>", borrar_texto1)
texto2.bind("<Button-1>", borrar_texto2)

# Crear el marco para los botones
marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=10)

# Crear los botones
boton1 = tk.Button(marco_botones, text="Cancel", font=("Arial", 16))
boton1.pack(side=tk.LEFT, padx=10) # Ajustar el espacio entre widgets
boton2 = tk.Button(marco_botones, text="Add", font=("Arial", 16))
boton2.pack(side=tk.LEFT, padx=10) # Ajustar el espacio entre widgets

# Iniciar el ciclo principal de eventos
ventana.mainloop()
