# -*- coding: utf-8 -*-
"""
Created on Sun Dec 06 2020

@author: simslay
"""


import threading
# from tkinter import *
from game.game import Game
# from game.scorer import Scorer
from game.player.player import Player


def main():
    def play(game):
        deck = game.state.table.deck
        deck.shuffle()
        print("deck shuffled")
        print(deck)
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
        players = []

        for i in range(5):
            name = input("Please enter your name or press enter to end registering players:")

            if name == "":
                break

            players.append(Player(name, 100, 1000))

        while True:
            play(game0)

    # t1 = threading.Thread(target=run_app)
    # t1.start()
    t2 = threading.Thread(target=run_game_data)
    t2.start()


if __name__ == "__main__":
    main()
