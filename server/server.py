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
    global idCount
    conn.send(str.encode(str(p)))

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    p = 0
    idCount += 1

    start_new_thread(threaded_client, (conn, p, gameId))
