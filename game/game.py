# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from game.state import State


class Game(object):
    def __init__(self, players):
        self.game_over = False
        self.state = State()
        self.players = players
        self.current_player = players[0]
        self.turn_number = 1
        self.player_count = len(set(players))

    def display_players(self):
        for player in self.players:
            print(player.name)

    def change_player(self):
        self.turn_number += 1
        self.current_player = self.players[self.turn_number % self.player_count]
