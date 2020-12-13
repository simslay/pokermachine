# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from game.state import State


class Game(object):
    game_over = None
    state = None

    def __init__(self, starting_chips):
        self.starting_chips = starting_chips

    def init_game(self):
        self.game_over = False
        self.state = State()
        self.state.table.init_deck()
