# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from game.state import State


class Game(object):
    def __init__(self, starting_chips):
        self.game_over = False
        self.state = State()
        self.starting_chips = starting_chips
