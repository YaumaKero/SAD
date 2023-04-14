from client import Client
from gui import GUI

def main():
    # Crear una instancia del cliente
    client = Client("localhost", 8000)

    # Crear una instancia de la interfaz gráfica de usuario
    gui = GUI()

    # Ejecutar la interfaz gráfica de usuario
    gui.run()

if __name__ == "__main__":
    main()
