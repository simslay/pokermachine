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

    def __init__(self, starting_stake, starting_chips, small_blind, big_blind):
        self.starting_stake = starting_stake
        self.starting_chips = starting_chips
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.buy_in = starting_stake
        self.ready = False

    def init_game(self):
        self.game_over = False
        self.state = State()
        self.state.table.init_deck()

    def connected(self):
        return self.ready

    def act_one(self):
        state = self.state

        self.init_blinds()
        state.table.deck.shuffle()
        state.deal_hole()

        self.ask_players()

    def ask_players(self):
        state = self.state
        state.current_player = state.players_not_out[state.current_player_index]

        for player in state.players_not_out:
            player.action_done = False

        # while True:
        #     if state.current_player.action_done:
        #         break
        # while True:
        #     state.current_player
        #     if player_ready:
        #         state.ready_list.append(state.current_player)
        #     if len(state.ready_list) == len(state.players_not_out):
        #         break
        #     state.current_player_index += 1
        #     state.current_player_index %= len(state.players_not_out)
        #     state.current_player = state.players_not_out[state.current_player_index]

    def init_players_not_out(self):
        state = self.state

        for player in state.players:
            if player.stake >= 0 or player.first_hand and player.stake == self.buy_in:
                state.players_not_out.append(player)

    def init_dealer(self):
        state = self.state

        state.dealer_index = randrange(state.player_count)
        state.dealer = state.players_not_out[state.dealer_index]

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
            state.small_blind_player = state.players_not_out[state.dealer_index]
            state.big_blind_player = state.players_not_out[big_blind_index]

            state.small_blind_player.stake -= self.small_blind
            state.big_blind_player.stake -= self.big_blind
            state.big_blind_index = big_blind_index
        else:
            big_blind_index = (state.dealer_index + 2) % state.player_count
            state.small_blind_player = state.players_not_out[(state.dealer_index + 1) % state.player_count]
            state.big_blind_player = state.players_not_out[big_blind_index]

            state.small_blind_player.stake -= self.small_blind
            state.big_blind_player.stake -= self.big_blind
            state.big_blind_index = big_blind_index

        state.small_blind_player.bet = self.small_blind
        state.big_blind_player.bet = self.big_blind

        state.current_bet = self.big_blind

        state.pot += self.small_blind + self.big_blind

    def change_current_player(self):
        state = self.state

        if state.current_player.action_done:
            state.current_player_index = (state.current_player_index + 1) % len(state.players_not_out)
            state.current_player = state.players_not_out[state.current_player_index]

    def get_player(self, name):
        for player in self.state.players:
            if player.name == name:
                return player
        return None
