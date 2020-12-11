# -*- coding: utf-8 -*-
"""
Created on Mon Thu 07 17:58:00 2020

@author: simslay
"""

from tkinter import *
from gui.pygame_page import PygamePage


class StartPage(Frame):
    def __init__(self, parent, controller, response_q, game_event):
        Frame.__init__(self, parent)

        self.response_q = response_q
        self.game_event = game_event

        height = 500
        width = 800
        canvas = Canvas(self, height=height, width=width, bg="light green")
        canvas.pack()

        top_frame = Frame(canvas, bg='green', bd=5)
        top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2, anchor='nw')
        name_frame = Frame(top_frame, bg="light green", bd=5)
        name_frame.place(relx=0.5, rely=0.27, relwidth=0.9, relheight=0.5, anchor="n")
        self.entry_p0 = Entry(name_frame, font=("Courier", 12), bd=3)
        self.entry_p0.place(relwidth=0.2, relheight=1)
        self.entry_p1 = Entry(name_frame, font=("Courier", 12), bd=3)
        self.entry_p1.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)
        self.entry_p2 = Entry(name_frame, font=("Courier", 12), bd=3)
        self.entry_p2.place(relx=0.4, rely=0, relwidth=0.2, relheight=1)
        self.entry_p3 = Entry(name_frame, font=("Courier", 12), bd=3)
        self.entry_p3.place(relx=0.6, rely=0, relwidth=0.2, relheight=1)
        self.entry_p4 = Entry(name_frame, font=("Courier", 12), bd=3)
        self.entry_p4.place(relx=0.8, rely=0, relwidth=0.2, relheight=1)
        enter_player_label = Label(top_frame, text="Player Names:", font=("Courier", 12), bd=3)
        enter_player_label.place(relx=0.25, rely=0.07, relwidth=0.5, relheight=0.15)
        # self.entry.bind("<Return>", lambda _: self.button_click(self.entry.get()))

        bottom_frame = Frame(canvas, bg='green', bd=5)
        bottom_frame.place(relx=0.5, rely=1, relwidth=1, relheight=0.8, anchor='s')

        button = Button(bottom_frame, text="START", font=("Courier", 12),
                        command=lambda: self.button_click(self.entry_p0.get(), self.entry_p1.get(),
                                                          self.entry_p2.get(), self.entry_p3.get(),
                                                          self.entry_p4.get(), controller))
        button.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.2, anchor="n")

    def button_click(self, entry0, entry1, entry2, entry3, entry4, controller):
        player_entry_list = [entry0, entry1, entry2, entry3, entry4]
        player_entry_dict = {}

        for player in player_entry_list:
            if player != "":
                player_entry_dict[player] = None

        player_entry_list = list(player_entry_dict.keys())

        if len(player_entry_list) < 2:
            print("not enough players")
            return

        chip_entry_list = [100, 1000, 1, 2]

        setup = {
            "players": player_entry_list,
            "chips": chip_entry_list
        }

        self.response_q.put(setup)
        self.game_event.set()
        PygamePage()
