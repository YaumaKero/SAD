import socket
import threading
import pickle

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.clients = []
        self.decks = {}

    def start(self):
        self.socket.listen()
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.socket.accept()
            print(f"New client connected from {client_address}")
            self.clients.append(client_socket)
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                data = client_socket.recv(4096)
                if data:
                    message = pickle.loads(data)
                    if message["action"] == "add_deck":
                        self.decks[message["deck_name"]] = []
                    elif message["action"] == "add_card":
                        self.decks[message["deck_name"]].append(message["card"])
                    elif message["action"] == "get_decks":
                        response = {"decks": list(self.decks.keys())}
                        client_socket.send(pickle.dumps(response))
                    elif message["action"] == "get_cards":
                        deck_name = message["deck_name"]
                        response = {"cards": self.decks[deck_name]}
                        client_socket.send(pickle.dumps(response))
            except Exception as e:
                print(f"Error handling client: {e}")
                self.clients.remove(client_socket)
                client_socket.close()
                break
