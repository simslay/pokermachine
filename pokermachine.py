# -*- coding: utf-8 -*-
"""
Created on Sun Dec 06 2020

@author: simslay
"""


import threading
import queue
import time
from tkinter import *
from game.game import Game
# from game.scorer import Scorer
from game.player.player import Player


def main():
    class StartPage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)
            pass

    def play(game):
        state = game.state
        game_info_q.put(game)
        state.deal_hole()
        state.print_round_info()

        if not state.round_ended:
            state.deal_flop()
            state.print_round_info()
        if not state.round_ended:
            state.ask_players()

        game_info_q.put(game)
        state.print_round_info()
        state.round_ended = True
        state.end_round()

        print()

        print("It's " + state.current_player.name + "'s turn")

        state.change_player()
        input("Press enter to continue...")

    class App(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)

            container = Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            frames = [StartPage]

            frame = frames[0](container, self)
            self.frames[frames[0]] = frame
            frame.grid(row=0, column=0, sticky="nsew")

            self.fresh = True
            self.show_frame(StartPage)

        def show_frame(self, context):
            frame = self.frames[context]
            print("waiting")
            if not self.fresh:
                time.sleep(0.1)
                frame.update(game_info_q.get())
            self.fresh = False
            frame.tkraise()

    def run_app():
        app = App()
        app.mainloop()

    def run_game_data():
        players = []

        for i in range(5):
            name = input("Please enter your name or press enter to end registering players:")

            if name == "":
                break

            players.append(Player(name, 100, 1000))

        game0 = Game(players)
        state0 = game0.state
        state0.display_players()

        deck = game0.state.table.deck
        deck.shuffle()
        print("deck shuffled")
        print(deck)
        print()

        while True:
            play(game0)

    game_event = threading.Event()
    response_q = queue.Queue()
    game_info_q = queue.Queue()
    t1 = threading.Thread(target=run_app)
    t1.start()
    t2 = threading.Thread(target=run_game_data)
    t2.start()


if __name__ == "__main__":
    main()
