# game.py

"""
Classe représentant la logique du jeu de mémoire.
Elle contient les fonctions de gestion des cartes, du score et des tours.
"""

import random
import tkinter as tk
from card import Card


class Game:
    """
    Classe principale pour la gestion de la logique du jeu de mémoire.
    """

    def __init__(self, root, canvas):
        """
        Initialise le jeu avec une grille de cartes de taille spécifiée.

        Args:
            grid_size (int): La taille de la grille, par défaut 4 (4x4).
        """
        self.root = root
        self.canvas = canvas
        self.grid_size = 4
        self.score = 0
        self.essais = 0
        self.essais_label = tk.Label(self.root, text="Nombre de tentatives : " + str(self.essais))
        self.essais_label.pack()
        self.label_score = tk.Label(self.root, text="Score : " + str(self.score))
        self.label_score.pack()
        self.start()
    

    def start(self):
        self.flipped_cards = []
        self.finded_cards = []
        self.deck = self.create_deck()
        self.number_flips = 0
        self.score = 0
        self.update()

    def create_deck(self):
        value = []
        deck = []
        for i in range(self.grid_size**2):
            value.append(i+1)
        for i in range(self.grid_size**2):
            ran = random.choice(value)
            value.remove(ran)
            if i <=3:
                deck.append(Card(self.root, self.canvas, ran, 70 + i*120 , 70 + (i//4) *120))
            if i <= 7:
                deck.append(Card(self.root, self.canvas, ran, 70 + (i-4)*120 , 70 + (i//4) *120))
            if i <= 11:
                deck.append(Card(self.root, self.canvas, ran, 70 + (i-8)*120 , 70 + (i//4) *120))
            if i <= 15:
                deck.append(Card(self.root, self.canvas, ran, 70 + (i-12)*120 , 70 + (i//4) *120))
        return deck
    
    def check_pairs(self):
        if self.number_flips == 2:
            self.essais += 1
            self.essais_label.config(text="Nombre de tentatives : " + str(self.essais))
            card1= self.flipped_cards[0]
            card2= self.flipped_cards[1]
            self.unbind_all_cards()
            print(card1.value)
            print(card2.value)
            if card1.value ==  card2.value - 8 or card2.value == card1.value - 8:
                self.score += 1
                self.label_score.config(text="Score : " + str(self.score))
                self.flipped_cards = []
                self.finded_cards.append(card1)
                self.finded_cards.append(card2)
                self.win()
            else:
                card1.flip(True)
                card2.flip(True)
                self.flipped_cards = []
            self.number_flips = 0
            self.root.after(500, self.bind_all_cards)

    def add_number_flips(self):
        for card in self.deck:
            if card not in self.finded_cards:
                if card.is_flipped:
                    if card not in self.flipped_cards:
                        self.flipped_cards.append(card)
                        self.number_flips += 1

    def unbind_all_cards(self):
        for card in self.deck:
            card.unclickable()

    def bind_all_cards(self):
        for card in self.deck:
            if card not in self.finded_cards:
                card.clickable()
        
    def win(self):
        print(len(self.finded_cards))
        print(len(self.deck))
        if len(self.finded_cards) == self.grid_size**2:
            self.canvas.delete('all')
            self.label = tk.Label(self.root, text='Bravo ! Tu as trouvé toutes les cartes !')
            self.label.pack()

    def update(self):
        self.add_number_flips()
        self.check_pairs()
        self.root.after(16, self.update)
                




            
        


        