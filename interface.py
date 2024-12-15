# interface.py

"""
Classe représentant l'interface graphique du jeu de mémoire avec Tkinter.
Elle gère la présentation du jeu et l'interaction avec l'utilisateur.
"""

import tkinter as tk
from game import Game

class Interface():
    """
    Classe pour l'interface graphique du jeu de mémoire avec Tkinter.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Card Game")
        self.root.geometry("500x600")
        self.canvas = tk.Canvas(self.root, width=500, height=500, background='ivory')
        self.button = tk.Button(self.root, text="New Game", command=self.start)
        self.canvas.pack()
        self.button.pack()
    
    def start(self):
        self.canvas.delete('all')
        self.game = Game(self.root, self.canvas)     




            








    