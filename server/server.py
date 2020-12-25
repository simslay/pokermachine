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


def threaded_client(conn):
    print("New client thread started")
    global idCount

    conn.send(str.encode(str("OK")))

    while True:
        try:
            # print("Waiting...")
            data = conn.recv(4096).decode()

            if not data:
                break
            else:
                # print("Received", data)

                if data.startswith("name/"):
                    tab = data.split("/")
                    game.state.players.append(Player(tab[1], 100, 1000))

                    if idCount == 2 or game.game_over:
                        state = game.state
                        game.init_players_not_out()
                        state.player_count = len(state.players_not_out)
                        game.init_dealer()
                        print("Dealer: " + str(state.dealer))
                        game.init_current_player()
                        print("Current player: " + str(state.current_player))
                        game.ready = True
                        print("Act one")
                        game.act_one()

                if data.startswith("action/"):
                    state = game.state

                    if data.startswith("action/fold/"):
                        name = data.split("/")[2]
                        player = game.get_player(name)
                        player.fold = True
                        player.action_done = True
                        state.players_not_out.remove(player)

                    if data.startswith("action/call"):
                        name = data.split("/")[2]
                        player = game.get_player(name)
                        player.call = True
                        player.action_done = True
                        state.pot += state.current_bet-player.bet
                        player.stake -= state.current_bet-player.bet
                        player.bet = state.current_bet

                    if data.startswith("action/raise"):
                        split_str = data.split("/")
                        amount = int(split_str[2])
                        name = split_str[3]
                        player = game.get_player(name)
                        player.raised = True
                        player.action_done = True
                        state.current_bet += amount - player.bet
                        state.pot += amount
                        player.stake -= amount
                        player.bet += amount

                    if len(state.players_not_out) > 1:
                        game.change_current_player()
                    else:
                        game.game_over = True

                    print("current player:", game.state.current_player.name)

                conn.sendall(pickle.dumps(game))
        except Exception as e:
            print("server.py --> [EXCEPTION]:", str(e))
            break

    print("Lost connection")


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1

    if idCount == 1:
        print("Create game")
        game = Game(100, 1000, 1, 2)
        game.init_game()

    start_new_thread(threaded_client, (conn,))
