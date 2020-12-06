import random
import threading
import queue
from tkinter import *


def main():
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
            self.need_raise_info = False
            self.deck = StandardDeck()

    def play(game):
        game.deck.shuffle()

    class App(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)

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
    t1 = threading.Thread(target=run_app)
    t1.start()
    t2 = threading.Thread(target=run_game_data())
    t2.start()


if __name__ == "__main__":
    main()
