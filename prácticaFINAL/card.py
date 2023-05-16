import random

class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.priority = 10

    # Gets y sets 
    def get_front(self):
        return self.front

    def get_back(self):
        return self.back
    
    def set_front(self, new_front):
        self.front = new_front

    def set_back(self, new_back):
        self.back = new_back

    # Mezclar tarjetas aleatoriamente
    def shuffle(self):
        random.shuffle(self.cards)
    # Incrementar prioridad al fallar
    def fail(self):
        if self.priority > 1:
            self.priority -= 1
    # Decrementar prioridad al acertar
    def good(self):
        self.priority += 1
    # Borrar tarjeta
    def remove(self):
        self.cards.remove(self)

        

    
