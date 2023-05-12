import random

class Card:
    def __init__(self, front, back):
        self.front = front
        self.back = back
        self.priority = 1

    #los gets----------------------------------------------------------------   
    def get_front(self):
        return self.front

    def get_back(self):
        return self.back

    #los sets----------------------------------------------------------------
    def set_front(self, new_front):
        self.front = new_front

    def set_back(self, new_back):
        self.back = new_back

    #Funciones en modo Study------------------------------------------------

    #set el orden de aparicion de las cartas a random
    def shuffle(self):
        random.shuffle(self.cards)
    #boton Fail, aumenta prioridad en 1
    def fail(self):
        self.priority += 1
    #boton Good, reduce prioridad en -1
    def good(self):
        if self.priority > 1:
            self.priority -= 1
    #boton Remove, elimina la carta del deck
    def remove(self):
        self.cards.remove(self)
    #boton ShowBack
    def show_back(self):
        return self.back 

    #Funciones en modo AddCard------------------------------------------------
    
    #entrar por tecladod el front y back
    def add_front(self):
        input_text = input("Write front of the card: ")
        self.front += input_text 
    def add_back(self):
        input_text = input("Write back of the card: ")
        self.back += input_text 
    #funcion que cancela la accion de añadir carta y vuelve al menu
    def cancel(self):
        pass    
    #funcion que añade la carta al deck
    def add_card(self, deck):
        deck.add_card(self)
        

    
