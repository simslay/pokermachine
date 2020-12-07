# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from game.table.table import Table


class Game(object):
    def __init__(self):
        self.game_over = False
        self.table = Table(5)
