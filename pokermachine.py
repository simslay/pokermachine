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
from gui.start_page import StartPage
from gui.game_page import GamePage


def main():
    def play(game):
        state = game.state
        game.act_one()
        game_info_q.put(game)

        # state.display_players()

        # if not state.round_ended:
        #     state.deal_flop()
            # state.print_round_info()
            # print()
        # if not state.round_ended:
        #     state.ask_players()

        # game_info_q.put(game)
        # state.print_round_info()
        # print()

        # print("It's " + state.current_player.name + "'s turn")
        # state.change_player()

        state.round_ended = True
        state.end_round()

        # print()
        input("Press enter to continue...")

        game.init_game()

    class App(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)

            container = Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            list_of_frames = [StartPage, GamePage]

            for F in list_of_frames:
                frame = F(container, self, response_q, game_info_q, game_event)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.fresh = True
            self.show_frame(StartPage)

        def show_frame(self, context):
            frame = self.frames[context]
            print("waiting")
            if not self.fresh:
                time.sleep(0.1)
                frame.update_frame(game_info_q.get())
            self.fresh = False
            frame.tkraise()

    def run_app():
        app = App()
        app.mainloop()

    # from game data to app
    def ask_app(question, game=""):
        print("asking...")
        print(question)
        answer = ""
        if game != "":
            game_info_q.put(game)

        game_event.wait()
        if not response_q.empty():
            answer = response_q.get()
        game_event.clear()

        return answer

    def run_game_data():
        setup = ask_app("Start?")
        chips = setup["chips"]
        players_name = setup["players"]
        game0 = Game(chips[0], chips[1], chips[2], chips[3])
        game0.init_game()
        state0 = game0.state
        state0.setup = setup
        state0.players = [Player(name, chips[0], chips[1]) for name in players_name if name != ""]
        state0.players_not_out = state0.players

        state0.current_player = state0.players[0]
        state0.player_count = len(state0.players)

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
