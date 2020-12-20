# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:23:00 2020

@author: simslay
"""

import socket
from _thread import *
import pickle
from game.game import Game
from game.player.player import Player

server = "192.168.79.1"
port = 5555
idCount = 0
game = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Server Started. Waiting for a connection")


def threaded_client(conn, p):
    print("New client thread started")
    global idCount
    print("Send", str(p))
    conn.send(str.encode(str(p)))

    while True:
        try:
            # print("Waiting...")
            data = conn.recv(4096).decode()

            if not data:
                break
            else:
                print("Received", data)

                if game.connected():
                    pass

                if data.startswith("name/"):
                    tab = data.split("/")
                    game.state.players.append(Player(tab[1], 100, 1000))
                    # print("Players:", str(game.state.players))

                    if idCount == 2:
                        state = game.state
                        state.players_not_out = state.players
                        # state.current_player = state.players[0]
                        state.player_count = len(state.players)
                        game.init_dealer()
                        game.init_current_player()
                        game.ready = True
                        print("Act one")
                        game.act_one()
                if data == "get/":
                    pass
                    # print("Players:", str(game.state.players))
                if data.startswith("fold/"):
                    name = data.split("/")[1]
                    player = game.get_player(name)
                    player.fold = True
                    player.action_done = True

                # print("Send game")
                conn.sendall(pickle.dumps(game))
        except Exception as e:
            print("Error:", str(e))
            break

    print("Lost connection")


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0

    if idCount == 2:
        # state = game.state
        # state.players.append(Player(name, 100, 1000))
        p = 1
    else:
        print("Create game")
        game = Game(100, 1000, 1, 2)
        game.init_game()
        # state = game.state
        # state.players.append(Player(name, 100, 1000))
        # state.setup = setup
        # chips = setup["chips"]
        # players_name = setup["players"]

    start_new_thread(threaded_client, (conn, p))
