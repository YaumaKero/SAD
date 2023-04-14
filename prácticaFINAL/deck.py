from card import Card
import random

class Deck:
    def __init__(self, name):
        self.cards = []
        self.name = name
    
    def add_card(self, card):
        self.cards.append(card)
    
    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort(key=lambda card: (card.priority, card.front))
