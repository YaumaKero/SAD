import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Flashcards App")

        self.button = tk.Button(self.root, text="Click me!", command=self.button_clicked)
        self.button.pack()

    def button_clicked(self):
        print("Hello, World!")

    def run(self):
        self.root.mainloop()

    def show_next_card(self, deck):