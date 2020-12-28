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
import traceback

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
    global game

    conn.send(str.encode(str("OK")))

    while True:
        try:
            data = conn.recv(4096).decode()

            if not data:
                break
            else:
                if data == "nextgame/":
                    if game.game_over or not game.init:
                        players = game.state.players
                        for player in players:
                            player.first_hand = False
                        game.init_game()
                        game.state.players = players
                        init_game()
                        print("Next act one")
                        game.act_one()

                if data.startswith("name/"):
                    tab = data.split("/")
                    game.state.players.append(Player(tab[1], 100, 1000))

                    if idCount == 2:
                        init_game()
                        print("First act one")
                        game.act_one()

                if data.startswith("action/"):
                    state = game.state

                    if data.startswith("action/fold/"):
                        name = data.split("/")[2]
                        player = game.get_player(name)
                        player.fold = True
                        player.action_done = True
                        state.players_not_out.remove(player)

                    if data.startswith("action/check/"):
                        name = data.split("/")[2]
                        player = game.get_player(name)
                        player.check = True
                        player.action_done = True

                    if data.startswith("action/bet/"):
                        split_str = data.split("/")
                        amount = split_str[2]
                        name = split_str[3]
                        player = game.get_player(name)
                        player.bet_bool = True
                        player.action_done = True
                        state.current_bet = amount
                        state.pot += amount
                        player.stake -= amount
                        player.bet = amount

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
                        state.current_bet = amount
                        state.pot += amount-player.bet
                        player.stake -= (amount-player.bet)
                        player.bet = amount

                    if len(state.players_not_out) > 1:
                        game.change_current_player()
                        game.ready = True
                    else:
                        game.game_over = True

                conn.sendall(pickle.dumps(game))
        except Exception as e:
            print("server.py --> [EXCEPTION]:", str(e))
            traceback.print_exc()
            break

    print("Lost connection")


def init_game():
    global game

    print("init_game()")

    state = game.state
    game.init_players_not_out()
    state.player_count = len(state.players_not_out)
    game.init_dealer()
    print("Dealer: " + str(state.dealer))
    game.init_current_player()
    print("Current player: " + str(state.current_player))
    game.ready = True
    game.game_over = False
    game.init = True


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1

    if idCount == 1:
        print("Create game")
        game = Game(100, 1000, 1, 2)
        game.init_game()

    start_new_thread(threaded_client, (conn,))
