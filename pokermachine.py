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

            height = 500
            width = 800
            canvas = Canvas(self, height=height, width=width, bg="light green")
            canvas.pack()

            left_frame = Frame(canvas, bg='green', bd=5)
            left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1, anchor='nw')
            name_frame = Frame(left_frame, bg="light green", bd=5)
            name_frame.place(relx=0.5, rely=0.17, relwidth=0.9, relheight=0.7, anchor="n")
            self.entry_p0 = Entry(name_frame, font=("Courier", 12), bd=3)
            self.entry_p0.place(relwidth=0.5, relheight=0.2)
            self.entry_p1 = Entry(name_frame, font=("Courier", 12), bd=3)
            self.entry_p1.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)
            self.entry_p2 = Entry(name_frame, font=("Courier", 12), bd=3)
            self.entry_p2.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.2)
            self.entry_p3 = Entry(name_frame, font=("Courier", 12), bd=3)
            self.entry_p3.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.2)
            self.entry_p4 = Entry(name_frame, font=("Courier", 12), bd=3)
            self.entry_p4.place(relx=0, rely=0.4, relwidth=0.5, relheight=0.2)
            enter_player_label = Label(left_frame, text="Player Names:", font=("Courier", 12), bd=3)
            enter_player_label.place(relx=0.25, rely=0.07, relwidth=0.5, relheight=0.05)
            # self.entry.bind("<Return>", lambda _: self.button_click(self.entry.get()))

            right_frame = Frame(canvas, bg='green', bd=5)
            right_frame.place(relx=1, rely=0, relwidth=0.5, relheight=1, anchor='ne')

            button = Button(right_frame, text="START", font=("Courier", 12),
                            command=lambda: self.button_click(self.entry_p0.get(), self.entry_p1.get(),
                                                              self.entry_p2.get(), self.entry_p3.get(),
                                                              self.entry_p4.get(), controller))
            button.place(relx=0.5, rely=0.9, relwidth=0.3, relheight=0.1, anchor="n")

        @staticmethod
        def button_click(entry0, entry1, entry2, entry3, entry4, controller):
            entry_list = [entry0, entry1, entry2, entry3, entry4]
            player_entry_list = [entry0, entry1, entry2, entry3, entry4]
            player_entry_list = list(set(player_entry_list))
            for player in player_entry_list:
                if player == "":
                    player_entry_list.remove(player)
            if len(player_entry_list) < 2:
                print("not enough players")
                return
            chip_entry_list = [100, 1000, 1, 2]

            setup = {
                "players": player_entry_list,
                "chips": chip_entry_list
            }
            response_q.put(setup)
            game_event.set()
            # controller.show_frame(GamePage)

    class GamePage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)

        def update_frame(self, game):
            pass

    def play(game):
        state = game.state
        game_info_q.put(game)
        state.deal_hole()
        state.print_round_info()
        print()

        if not state.round_ended:
            state.deal_flop()
            state.print_round_info()
            print()
        if not state.round_ended:
            state.ask_players()

        game_info_q.put(game)
        state.print_round_info()
        print()
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

            list_of_frames = [StartPage, GamePage]

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
                frame.update_frame(game_info_q.get())
            self.fresh = False
            frame.tkraise()

    def run_app():
        app = App()
        app.mainloop()

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
        game0 = Game()
        state0 = game0.state
        state0.setup = ask_app("Start?")
        players_name = state0.setup["players"]
        chips = state0.setup["chips"]
        state0.players = [Player(name, chips[0], chips[1]) for name in players_name if name != ""]
        # state0.display_players()

        state0.current_player = state0.players[0]
        state0.player_count = len(set(state0.players))

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
