# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from game.state import State


class Game(object):
    def __init__(self, players):
        self.game_over = False
        self.state = State(players)
        self.round_ended = False
