# -*- coding: utf-8 -*-
"""
Created on Sun Dec 06 2020

@author: simslay
"""


import threading
from tkinter import *
from game.game import Game
from game.scorer import Scorer


def main():
    def play(game):
        game.table.deck.shuffle()
        print(game.table.deck)
        input("Press enter to continue...")

    # class App(Tk):
    #     def __init__(self, *args, **kwargs):
    #         Tk.__init__(self, *args, **kwargs)
    #         self.game_object = object

    # def run_app():
    #     app = App()
    #     app.mainloop()

    def run_game_data():
        game0 = Game()

        while True:
            play(game0)

    # t1 = threading.Thread(target=run_app)
    # t1.start()
    t2 = threading.Thread(target=run_game_data)
    t2.start()


if __name__ == "__main__":
    main()
