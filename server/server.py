# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 14:23:00 2020

@author: simslay
"""

import socket
from _thread import *
import pickle

server = "192.168.0.11"
port = 5555
idCount = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Server Started. Waiting for a connection")


def threaded_client(conn, p, gameId):
    print("New client thread started")
    global idCount
    conn.send(str.encode(str(p)))

    while True:
        try:
            data = conn.recv(4096).decode()
        except:
            break

    print("Lost connection")

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1) // 2

    start_new_thread(threaded_client, (conn, p, gameId))
