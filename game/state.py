# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from game.table.table import Table


class State:
    def __init__(self, players):
        self.table = Table(5)
        self.players = players
        self.current_player = players[0]
        self.turn_number = 1
        self.player_count = len(set(players))

    def deal_flop(self):
        deck = self.table.deck

        deck.burn()
        deck.deal(self.table, 3)

    def display_players(self):
        for player in self.players:
            print(player.name)

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
        print(f"Community cards: {self.table.community_cards}")
