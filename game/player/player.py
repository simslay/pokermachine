# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""


class Player(object):
    def __init__(self, name, chips, stake):
        self.name = name
        self.chips = chips
        self.stake = stake
        self.cards = []

    def __repr__(self):
        return self.name
