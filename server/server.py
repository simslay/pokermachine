# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:23:00 2020

@author: simslay
"""

import socket
from _thread import *
import pickle
from game.game import Game

server = "192.168.0.11"
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
    conn.send(str.encode(str(p)))

    while True:
        try:
            data = conn.recv(4096).decode()

            if not data:
                break
            else:
                # print("Sending game")
                conn.sendall(pickle.dumps(game))
        except:
            break

    print("Lost connection")

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0

    if idCount == 2:
        game.ready = True
        p = 1
    else:
        game = Game(100, 1000, 1, 2)

    start_new_thread(threaded_client, (conn, p))
