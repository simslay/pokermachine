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

    def __init__(self, conn, starting_chips, starting_stake, small_blind, big_blind):
        self.conn = conn
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

        self.init_dealer()
        print("Dealer: " + str(state.dealer))
        self.init_blinds()
        state.table.deck.shuffle()
        state.deal_hole()

        self.init_dealer()
        self.init_current_player()

        # self.ask_players()

        # self.state.pot += self.small_blind + self.big_blind

    def ask_players(self):
        state = self.state

        for player in state.players_not_out:
            player.ready = False

        while True:
            player_ready = self.answer(state.players_not_out[state.current_player_index])
            state.current_player_index += 1
            state.current_player_index %= len(state.players_not_out)
            state.current_player = state.players_not_out[state.current_player_index]
            if player_ready:
                state.ready_list.append(state.current_player)
            if len(state.ready_list) == len(state.players_not_out):
                break

    def answer(self, player):
        state = self.state

        return True

    def init_dealer(self):
        state = self.state

        state.dealer_index = randrange(state.player_count)
        state.dealer = state.players[state.dealer_index]

    def init_current_player(self):
        state = self.state

        if state.player_count == 2:
            state.current_player_index = state.dealer_index
        else:
            state.current_player_index = (state.dealer_index + 3) % len(state.players_not_out)

        state.current_player = state.players_not_out[state.current_player_index]

    def init_blinds(self):
        state = self.state

        if state.player_count == 2:
            big_blind_index = (state.dealer_index + 1) % 2
            state.small_blind_player = state.players[state.dealer_index]
            state.big_blind_player = state.players[big_blind_index]

            state.small_blind_player.chips -= self.small_blind
            state.big_blind_player.chips -= self.big_blind
            state.big_blind_index = big_blind_index
        else:
            big_blind_index = (state.dealer_index + 2) % state.player_count
            state.small_blind_player = state.players[(state.dealer_index + 1) % state.player_count]
            state.big_blind_player = state.players[big_blind_index]

            state.small_blind_player.chips -= self.small_blind
            state.big_blind_player.chips -= self.big_blind
            state.big_blind_index = big_blind_index
