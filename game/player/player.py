# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""


class Player(object):
    def __init__(self, name, stake, chips):
        self.name = name
        self.stake = stake
        self.chips = chips
        self.cards = []
        self.fold = False
        self.all_in = False
        self.ready = False
        self.action_done = False
        self.first_hand = True

    def __repr__(self):
        res = "Player[name=" + self.name + ", fold=" + str(self.fold) + "]"

        return self.name
