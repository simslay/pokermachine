# -*- coding: utf-8 -*-
"""
Created on Mon Dec 07 17:20:00 2020

@author: simslay
"""

from game.state import State
from game.player.player import Player


class Game(object):
    game_over = None
    state = None

    def __init__(self, starting_chips):
        self.small_blind_amount = 1
        self.big_blind_amount = 2
        self.small_blind = Player()
        self.big_blind = Player()
        self.first_actor = Player()
        self.acting_player = Player()
        self.starting_chips = starting_chips
        self.ready_list = []
        self.highest_stake = 0

    def init_game(self):
        self.game_over = False
        self.state = State()
        self.state.table.init_deck()

    def act_one(self):
        if self.small_blind_amount > self.small_blind.chips:
            self.small_blind.stake += self.small_blind.chips
            self.highest_stake = self.small_blind.chips
            self.state.pot += self.small_blind.chips
            self.small_blind.chips = 0
            print(f"{self.small_blind.name} is all-in!")
            self.small_blind.all_in = True
        else:
            self.small_blind.chips -= self.small_blind_amount
            self.small_blind.stake += self.small_blind_amount
            self.highest_stake = self.small_blind_amount
            self.state.pot += self.small_blind_amount
        if self.big_blind_amount > self.big_blind.chips:
            self.big_blind.stake += self.big_blind.chips
            self.highest_stake = self.big_blind.chips
            self.state.pot += self.big_blind.chips
            self.big_blind.chips = 0
            print(f"{self.big_blind} is all-in!")
            self.big_blind.all_in = True
        else:
            self.big_blind.chips -= self.big_blind_amount
            self.big_blind.stake += self.big_blind_amount
            self.highest_stake = self.big_blind_amount
            self.pot += self.big_blind_amount
        self.ask_players()

    def ask_players(self):
        self.ready_list.clear()
        starting_index = self.state.players_not_out.index(self.first_actor)
        for player in self.state.players_not_out:
            player.ready = False
        while True:
            self.acting_player = self.state.players_not_out[starting_index]
            player_ready = self.answer(self.list_of_players_not_out[starting_index])
            starting_index += 1
            starting_index %= len(self.list_of_players_not_out)
            if player_ready:
                self.ready_list.append("gogo")
            if len(self.ready_list) == len(self.list_of_players_not_out):
                break

    def answer(self, player):
        player.stake_gap = self.highest_stake - player.stake
        if player.all_in or player.fold or self.fold_out:
            return True
        if player.chips <= 0:
            print(f"{player.name} is all in!")
            player.all_in = True
        print(f"Highest stake: {self.highest_stake}")
        print(f"Put in at least {player.stake_gap} to stay in.\nDon't Have that much? You'll have to go all-in!")
        print(f"Chips available: {player.chips}")
        self.possible_responses.clear()
        if player.stake_gap > 0:
            self.possible_responses.append("fold")
            if player.stake_gap == player.chips:
                self.possible_responses.append("all_in_exact")
            if player.stake_gap > player.chips:
                self.possible_responses.append("all_in_partial")
            if player.stake_gap < player.chips:
                self.possible_responses.append("call_exact")
                self.possible_responses.append("call_and_raise")
                self.possible_responses.append("call_and_all_in")
        if player.stake_gap == 0:
            self.possible_responses.append("check")
            self.possible_responses.append("raise")
            self.possible_responses.append("fold")
            self.possible_responses.append("all_in")
        while True:
            print(self.possible_responses)
            response = str(ask_app(f"{player}'s action\n->", self))
            if response not in self.possible_responses:
                print("Invalid response")
                continue
            if response == "all_in_partial":
                player.stake += player.chips
                self.pot += player.chips
                player.stake_gap -= player.chips
                player.chips = 0
                print(f"{player.name} is all-in!")
                player.all_in = True
                return True
            if response == "all_in_exact":
                print(f"{player.name} is all-in!")
                player.all_in = True
                player.stake += player.stake_gap
                self.pot += player.stake_gap
                player.chips = 0
                player.stake_gap = 0
                return True
            if response == "fold":
                player.fold = True
                self.fold_list.append(player)
                if len(self.fold_list) == (len(self.list_of_players_not_out) - 1):
                    for player in self.list_of_players_not_out:
                        if player not in self.fold_list:
                            self.fold_out = True
                            print(f"{player} wins!")
                            self.winners.append(player)
                            for player in self.winners:
                                player.win = True
                            self.round_ended = True
                return True
            if response == "call_exact":
                player.stake += player.stake_gap
                self.pot += player.stake_gap
                player.chips -= player.stake_gap
                player.stake_gap = 0
                return True
            if response == "check":
                player.stake_gap = 0
                return True
            if response == "raise":
                self.need_raise_info = True
                while True:
                    bet = int(
                        ask_app(f"How much would {player.name} like to raise? ({player.chips} available)\n->",
                                self))
                    if bet > player.chips or bet <= 0:
                        print("Invalid response")
                        continue
                    if bet == player.chips:
                        print(f"{player.name} is all-in!")
                        player.all_in = True
                    self.need_raise_info = False
                    player.stake += bet
                    self.pot += bet
                    player.chips -= bet
                    self.highest_stake = player.stake
                    self.ready_list.clear()
                    player.stake_gap = 0
                    return True
            if response == "call_and_raise":
                self.need_raise_info = True
                player.stake += player.stake_gap
                self.pot += player.stake_gap
                player.chips -= player.stake_gap
                player.stake_gap = 0
                while True:
                    try:
                        bet = int(
                            ask_app(f"How much would {player.name} like to raise? ({player.chips} available)\n->",
                                    self))
                    except ValueError:
                        continue
                    if bet > player.chips or bet <= 0:
                        print("Invalid response")
                        continue
                    if bet == player.chips:
                        print(f"{player.name} is all-in!")
                        player.all_in = True
                    self.need_raise_info = False
                    player.stake += bet
                    self.pot += bet
                    player.chips -= bet
                    self.highest_stake = player.stake
                    self.ready_list.clear()
                    return True
            if response == "call_and_all_in":
                player.stake += player.stake_gap
                self.pot += player.stake_gap
                player.chips -= player.stake_gap
                player.stake_gap = 0
                player.stake += player.chips
                self.pot += player.chips
                player.stake_gap -= player.chips
                player.chips = 0
                print(f"{player.name} is all-in!")
                player.all_in = True
                self.highest_stake = player.stake
                self.ready_list.clear()
                return True
            if response == "all_in":
                player.stake_gap = 0
                player.stake += player.chips
                self.pot += player.chips
                player.chips = 0
                print(f"{player.name} is all-in!")
                player.all_in = True
                self.highest_stake = player.stake
                self.ready_list.clear()
                return True
            print("Invalid Response")