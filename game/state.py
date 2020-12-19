# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from game.table.table import Table


class State:
    player_count = 0

    def __init__(self):
        self.table = Table(5)
        self.players = []
        self.current_player = None
        self.current_player_index = None
        self.dealer = None
        self.dealer_index = None
        self.small_blind_player = None
        self.big_blind_player = None
        self.big_blind_index = None
        self.turn_number = 1
        self.players_not_out = []
        self.round_ended = False
        self.setup = {}
        self.flop_dealt = False
        self.pot = 0
        self.ready_list = []
        self.fold_out = False

    def deal_flop(self):
        deck = self.table.deck

        deck.burn()
        deck.deal(self.table, 3)

        self.flop_dealt = True

    def display_players(self):
        for player in self.players:
            print(player)

    def change_player(self):
        self.current_player = self.players[self.turn_number % self.player_count]
        self.turn_number += 1

    def print_round_info(self):
        for player in self.players:
            print(f"Name: {player.name}")
            print(f"Cards: {player.cards}")
            # print(f"Player score: {player.score}")
            print(f"Chips: {player.chips}")
            # print(f"Special Attributes: {player.list_of_special_attributes}")
            if player.fold:
                print(f"Folded")
            if player.all_in:
                print(f"All-in")
            print(f"Stake: {player.stake}")
            # print(f"Stake-gap: {player.stake_gap}")
            print()
        print(f"Pot: {self.table.pot}")
        print(f"Community cards: {self.table.cards}")

    def ask_players(self):
        pass

    def deal_hole(self):
        for player in self.players_not_out:
            self.table.deck.deal(player, 2)

    def end_round(self):
        pass
