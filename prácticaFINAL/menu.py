from card import Card
from deck import Deck
import tkinter

class Menu:
    def __init__(self):
            self.decks = []

    def add_deck(self, name):
        try:
            # Si el objeto no está en la lista, lo agregamos
            if name not in [o.name for o in self.decks]:
                self.decks.append(Deck(name))
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
    
    def show_next_card(self, deck):
        

    