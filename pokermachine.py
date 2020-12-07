import random
import threading
import queue
from tkinter import *
from game.game import Game


def main():
    def play(game):
        game.table.deck.shuffle()
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
