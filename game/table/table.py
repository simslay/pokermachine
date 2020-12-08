# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from game.table.deck import Deck


class Table:
    def __init__(self, seats):
        self.seats = seats
        self.deck = Deck()
        self.community_cards = []
        self.pot = 0
