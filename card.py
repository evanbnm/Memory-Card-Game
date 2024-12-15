"""
File : card.py
Contains the Card class for the memory game.
"""
from PIL import Image, ImageTk
class Card:
    """
    Class representing a card in the memory game.
    """

    def __init__(self, root, canvas, value, x, y, is_flipped=False):
        """
        Initializes a card with a value and flipped status.

        Args:
            value (int): The value of the card.
            is_flipped (bool): The flipped status of the card, default is False.
        """
        self.root = root
        self.canvas = canvas
        self.value = value
        self.is_flipped = is_flipped
        self.x = x
        self.y = y
        self.unknown()

    def known(self):
        images = ["images/1.png", "images/2.png", "images/3.png", "images/4.png", "images/5.png", "images/6.png", "images/7.png", "images/8.png"]
        if self.value <= 8:
            original = Image.open(images[self.value - 1])
        if self.value > 8:
            original = Image.open(images[self.value - 9])
        
        resized = original.resize((100, 110))

        self.image = ImageTk.PhotoImage(resized)
        
        self.card = self.canvas.create_image(self.x, self.y, image=self.image)

    def unknown(self):
        original = Image.open("images/0.png")
        resized = original.resize((100, 110))

        self.image = ImageTk.PhotoImage(resized)

        self.card = self.canvas.create_image(self.x, self.y, image=self.image)
        self.clickable()

    def flip(self, event):
        """
        Flips the card to reveal its value.
        """
        if self.is_flipped:
            self.root.after(500, self.unknown)
        if not self.is_flipped:
            self.known()
        self.is_flipped = not self.is_flipped

    def clickable(self):
        self.canvas.tag_bind(self.card, '<1>', self.flip)

    def unclickable(self):
        self.canvas.tag_unbind(self.card, '<1>')

