from card import Card
import random

class Deck:
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.currentcard = None
    
    # Añadir tarjeta al mazo
    def add_card(self, front: str, back: str):
        if front!="" and back!="":
            self.cards.append(Card(front,back))
    
    # Eliminar tarjeta
    def remove_card(self, card):
        self.cards.remove(card)
    
    # Mezclar tarjetas aleatoriamente
    def shuffle(self):
        random.shuffle(self.cards)
    
    # Ordenar tarjetas por prioridad (de mayor a menor, siendo 1 la máxima prioridad)
    def sort(self):
        self.cards.sort(key=lambda card: (card.priority, card.front))
