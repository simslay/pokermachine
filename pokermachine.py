import random
import threading
import queue
from tkinter import *


def main():
    class Card(object):
        def __init__(self, value, suit):
            self.value = value
            self.suit = suit
            self.showing = True

        def __repr__(self):
            value_name = ""
            suit_name = ""
            if self.showing:
                if self.value == 0:
                    value_name = "Two"
                if self.value == 1:
                    value_name = "Three"
                if self.value == 2:
                    value_name = "Four"
                if self.value == 3:
                    value_name = "Five"
                if self.value == 4:
                    value_name = "Six"
                if self.value == 5:
                    value_name = "Seven"
                if self.value == 6:
                    value_name = "Eight"
                if self.value == 7:
                    value_name = "Nine"
                if self.value == 8:
                    value_name = "Ten"
                if self.value == 9:
                    value_name = "Jack"
                if self.value == 10:
                    value_name = "Queen"
                if self.value == 11:
                    value_name = "King"
                if self.value == 12:
                    value_name = "Ace"
                if self.suit == 0:
                    suit_name = "Diamonds"
                if self.suit == 1:
                    suit_name = "Clubs"
                if self.suit == 2:
                    suit_name = "Hearts"
                if self.suit == 3:
                    suit_name = "Spades"
                return value_name + " of " + suit_name
            else:
                return "[CARD]"

    class Player(object):
        def __init__(self, name, chips, stake):
            self.name = name
            self.chips = chips
            self.stake = stake
            self.cards = []

        def __repr__(self):
            return self.name

    class Table:
        def __init__(self, seats):
            self.seats = seats

    class StandardDeck(list):
        def __init__(self):
            super().__init__()
            suits = list(range(4))
            values = list(range(13))
            [[self.append(Card(i, j)) for j in suits] for i in values]

        def __repr__(self):
            return f"Standard deck of cards\n{len(self)} cards remaining"

        def shuffle(self):
            random.shuffle(self)
            print("\n\n--deck shuffled--")

        def deal(self, location, times=1):
            for i in range(times):
                location.cards.append(self.pop(0))

        def burn(self):
            self.pop(0)

    class Game(object):
        def __init__(self):
            self.deck = StandardDeck()
            self.game_over = False
            self.table = Table(5)

    def play(game):
        game.deck.shuffle()
        input("Press enter to continue...")

    class App(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)
            self.game_object = object

    def run_app():
        app = App()
        app.mainloop()

    def run_game_data():
        game0 = Game()

        while True:
            play(game0)

    game_event = threading.Event()
    response_q = queue.Queue()
    game_info_q = queue.Queue()
    end_update = threading.Event()
    # t1 = threading.Thread(target=run_app)
    # t1.start()
    t2 = threading.Thread(target=run_game_data)
    t2.start()


if __name__ == "__main__":
    main()
