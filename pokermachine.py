# -*- coding: utf-8 -*-
"""
Created on Sun Dec 06 2020

@author: simslay
"""


import time
from tkinter import *
from gui.start_page import StartPage


def main():
    def play(game):
        state = game.state
        game.act_one()
        # game_info_q.put(game)

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

        state.round_ended = True
        state.end_round()

        game.init_game()

    class App(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)

            container = Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            list_of_frames = [StartPage]

            for F in list_of_frames:
                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.fresh = True
            self.show_frame(StartPage)

        def show_frame(self, context):
            frame = self.frames[context]
            print("waiting")
            if not self.fresh:
                time.sleep(0.1)
                # frame.update_frame(game_info_q.get())
            self.fresh = False
            frame.tkraise()

    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
