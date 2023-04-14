import socket
import pickle
import deck

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.decks = []

    def send_message(self, message):
        try:
            self.socket.send(pickle.dumps(message))
            response = self.socket.recv(4096)
            return pickle.loads(response)
        except Exception as e:
            print(f"Error sending message: {e}")
            return None

    def init_decks(self):
        #aqui vamos a iniciar las barajas
        #las personales se quedan en un archivo, las colaborativas se importan del server

    def add_deck(self, name):
        try:
            # Si el objeto no está en la lista, lo agregamos
            if name not in [o.name for o in self.decks]:
                self.decks.append(deck.Deck(name))
                print(f"{name} added successfuly.")
            # Si el objeto ya está en la lista, lanzamos una excepción
            else:
                raise ValueError("This name is already used.")
        except ValueError as e:
            print(f"Error: {e}")

    def rmv_deck(self, deck):
        try:
            xdeck = next(xdeck for xdeck in self.decks if xdeck.name == deck.name)
            self.decks.remove(xdeck)
            print(f"{deck.name} successfuly removed.")
        except StopIteration:
            print(f"{deck.name} not found.")