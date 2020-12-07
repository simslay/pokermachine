# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.showing = True

    def __repr__(self):
        value_name = ""
        suit_name = ""
        if self.showing:
            if self.value == 0:
                value_name = "Two"
            if self.value == 1:
                value_name = "Three"
            if self.value == 2:
                value_name = "Four"
            if self.value == 3:
                value_name = "Five"
            if self.value == 4:
                value_name = "Six"
            if self.value == 5:
                value_name = "Seven"
            if self.value == 6:
                value_name = "Eight"
            if self.value == 7:
                value_name = "Nine"
            if self.value == 8:
                value_name = "Ten"
            if self.value == 9:
                value_name = "Jack"
            if self.value == 10:
                value_name = "Queen"
            if self.value == 11:
                value_name = "King"
            if self.value == 12:
                value_name = "Ace"
            if self.suit == 0:
                suit_name = "Diamonds"
            if self.suit == 1:
                suit_name = "Clubs"
            if self.suit == 2:
                suit_name = "Hearts"
            if self.suit == 3:
                suit_name = "Spades"
            return value_name + " of " + suit_name
        else:
            return "[CARD]"
