# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from game.table.table import Table


class State:
    def __init__(self):
        self.table = Table(5)
