import random
from game.card import Card


class Deck(list):
    def __init__(self):
        super().__init__()
        suits = list(range(4))
        values = list(range(13))
        [[self.append(Card(i, j)) for j in suits] for i in values]

    def __repr__(self):
        return f"Deck of cards\n{len(self)} cards remaining"

    def shuffle(self):
        random.shuffle(self)

    def deal(self, location, times=1):
        for i in range(times):
            location.community_cards.append(self.pop(0))

    def burn(self):
        self.pop(0)
