# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from random import randrange
from game.state import State
from game.player.player import Player


class Game(object):
    game_over = None
    state = None

    def __init__(self, starting_chips, starting_stake, small_blind, big_blind):
        self.starting_chips = starting_chips
        self.starting_stake = starting_stake
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.ready = False

    # def __repr__(self):
    #     return str(self.state.players[0].cards)

    def init_game(self):
        self.game_over = False
        self.state = State()
        self.state.table.init_deck()

    def connected(self):
        return self.ready

    def act_one(self):
        print("Enter act_one")
        state = self.state

        self.init_first_player()
        print("Dealer: " + str(state.first_player))
        self.init_blinds()
        state.table.deck.shuffle()
        state.deal_hole()
        self.ask_players()

    def ask_players(self):
        state = self.state

    def init_first_player(self):
        print("Enter init_first_player")
        state = self.state

        state.first_player_index = randrange(state.player_count)
        state.first_player = state.players[state.first_player_index]
        print("End of init_first_player")

    def init_blinds(self):
        state = self.state

        if state.player_count == 2:
            big_blind_index = (state.first_player_index + 1) % 2
            state.small_blind_player = state.players[state.first_player_index]
            state.big_blind_player = state.players[big_blind_index]

            state.small_blind_player.chips -= self.small_blind
            state.big_blind_player.chips -= self.big_blind
            state.big_blind_index = big_blind_index
        else:
            big_blind_index = (state.first_player_index+2)%state.player_count
            state.small_blind_player = state.players[(state.first_player_index+1)%state.player_count]
            state.big_blind_player = state.players[big_blind_index]

            state.small_blind_player.chips -= self.small_blind
            state.big_blind_player.chips -= self.big_blind
            state.big_blind_index = big_blind_index
