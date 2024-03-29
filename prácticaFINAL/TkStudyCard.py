import tkinter as tk
import deck

def exec(deck):
    # Ordeno las tarjetas por prioridad e impongo que la tarjeta actual es la primera
    deck.sort()
    deck.current_card = 0

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
    ventana.title("Study window ~ Flashcard Study Manager with AI")
    
    # Crear el marco para los textos
    marco_textos = tk.Frame(ventana)
    marco_textos.pack(pady=40)

    # Crear los campos de entrada de texto
    texto1 = tk.Entry(marco_textos, font=("Arial", 16),fg='black', bg='white', width=30)
    texto1.insert(0, deck.cards[deck.current_card].front)
    texto1.configure(state='readonly')
    texto1.pack(pady=10) # Ajustar el espacio entre widgets

    texto2 = tk.Entry(marco_textos, font=("Arial", 16), fg='grey', bg='white', width=30)
    texto2.insert(0, "Tap to see the back...")
    texto2.pack(pady=10) # Ajustar el espacio entre widgets

    # Defino comandos para borrar el texto de fondo al hacer clic
    def showback(event):       
        if texto2.get() == "Tap to see the back...":
            texto2.delete(0, "end")
            texto2.insert(0, deck.cards[deck.current_card].back)
            texto2.config(fg='black', state='readonly')
    # Asociar la función con el evento clic en la entrada de texto
    texto2.bind("<Button-1>", showback)

    # Defino comandos para siguiente carta
    def nextcard():
        if deck.current_card<len(deck.cards):
            texto1.configure(state='normal')
            texto1.delete(0, "end")
            texto1.insert(0, deck.cards[deck.current_card].front)
            texto1.configure(state='readonly')

            texto2.configure(state='normal')
            texto2.delete(0, "end")
            texto2.insert(0, "Tap to see the back...")

        else:
            texto1.configure(state='normal')
            texto1.delete(0, "end")
            texto1.insert(0, "Congratulations!")
            texto1.configure(state='readonly')

            texto2.configure(state='normal')
            texto2.delete(0, "end")
            texto2.insert(0, "You studied all cards.")
            texto2.configure(state='readonly')
    # Defino comandos de fallo
    def fail():
        deck.cards[deck.current_card].fail()
        deck.current_card = deck.current_card + 1
        nextcard()
    # Defino comandos de acierto
    def good():
        deck.cards[deck.current_card].good()
        deck.current_card = deck.current_card + 1
        nextcard()
    
    # Crear marco para los botones Fail y Good
    marco_botones2 = tk.Frame(ventana)
    marco_botones2.pack(pady=10)
    # Crear botones para Fail y Good
    boton4 = tk.Button(marco_botones2, text="Fail", font=("Arial", 16), command=fail)
    boton4.pack(side=tk.LEFT, padx=10) # Ajustar el espacio entre widgets
    boton5 = tk.Button(marco_botones2, text="Good", font=("Arial", 16), command=good)
    boton5.pack(side=tk.LEFT, padx=10) # Ajustar el espacio entre widgets

    # Defino comandos para borrar tarjeta
    def delete_card():
        deck.cards.remove(deck.cards[deck.current_card])
        nextcard()

    # Crear boton para eliminar tarjeta
    boton6 = tk.Button(ventana, text="Delete", font=("Arial", 16), command=delete_card)
    boton6.pack(side=tk.LEFT, padx=10) # Ajustar el espacio entre widgets

    # Iniciar el ciclo principal de eventos
    ventana.mainloop()
