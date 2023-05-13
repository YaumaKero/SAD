from card import Card
import random

class Deck:
    def __init__(self, name):
        self.cards = []
        self.name = name
    
    def add_card(self, front: str, back: str):
        if front!="" and back!="":
            self.cards.append(Card(front,back))
    
    def remove_card(self, card):
        #if card in self.cards:
        self.cards.remove(card)
    
    def shuffle(self):
        #barajar cartas del mazo para cada prioridad
        random.shuffle(self.cards)     
        
    
    def sort(self):
        self.cards.sort(key=lambda card: (card.priority, card.front))
