# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:58:00 2020

@author: simslay
"""

import tkinter as tk
from tkinter import *
from gui.pygame_page import PygamePage
from client.network import Network
import traceback


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        height = 500
        width = 800
        self.canvas = Canvas(self, height=height, width=width, bg="light green")
        self.canvas.pack()

        top_frame = Frame(self.canvas, bg='green', bd=5)
        top_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2, anchor='nw')
        name_frame = Frame(top_frame, bg="light green", bd=5)
        name_frame.place(relx=0.5, rely=0.27, relwidth=0.5, relheight=0.5, anchor="n")
        self.entry_p0 = Entry(name_frame, font=("Courier", 12), bd=3)
        self.entry_p0.place(relwidth=1, relheight=1)
        enter_player_label = Label(top_frame, text="Enter your name:", font=("Courier", 12), bd=3)
        enter_player_label.place(relx=0.25, rely=0.07, relwidth=0.5, relheight=0.15)
        # self.entry.bind("<Return>", lambda _: self.button_click(self.entry.get()))

        bottom_frame = Frame(self.canvas, bg='green', bd=5)
        bottom_frame.place(relx=0.5, rely=1, relwidth=1, relheight=0.8, anchor='s')

        button = Button(bottom_frame, text="START", font=("Courier", 12),
                        command=lambda: self.button_click(self.entry_p0.get(), controller))
        button.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.2, anchor="n")

    def button_click(self, entry0, controller):
        player_entry_list = [entry0]
        player_entry_dict = {}

        for player in player_entry_list:
            if player != "":
                player_entry_dict[player] = None

        player_entry_list = list(player_entry_dict.keys())

        print("Connect to server")
        n = Network(entry0)

        try:
            print("Receive game")
            game = n.send("name/" + entry0)
            print("Sent name/" + entry0)

            if not game.connected():
                print("Waiting for a new player...")
                while True:
                    game = n.send("get/")
                    if game.connected():
                        break

            controller.destroy()
            PygamePage(n, game, entry0)
        except Exception as e:
            print("start_page.py --> [EXCEPTION]:", str(e))
            traceback.print_exc()
            return
