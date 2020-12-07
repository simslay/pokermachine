class Scorer(object):
    def __init__(self, cards):
        self.cards = cards

    def flush(self):
        suits = [card.suit for card in self.cards]
        if len(set(suits)) == 1:
            return True
        return False

    def straight(self):
        values = [card.value for card in self.cards]
        values.sort()

        if not len(set(values)) == 5:
            return False

        if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
            return 5

        else:
            if not values[0] + 1 == values[1]:
                return False
            if not values[1] + 1 == values[2]:
                return False
            if not values[2] + 1 == values[3]:
                return False
            if not values[3] + 1 == values[4]:
                return False

        return values[4]

    def high_card(self):
        values = [card.value for card in self.cards]
        high_card = None
        for card in self.cards:
            if high_card is None:
                high_card = card
            elif high_card.value < card.value:
                high_card = card

        return high_card

    def highest_count(self):
        count = 0
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) > count:
                count = values.count(value)

        return count

    def pairs(self):
        pairs = []
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 2 and value not in pairs:
                pairs.append(value)

        return pairs

    def four_kind(self):
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 4:
                return True

    def full_house(self):
        two = False
        three = False

        values = [card.value for card in self.cards]
        if values.count(values) == 2:
            two = True
        elif values.count(values) == 3:
            three = True

        if two and three:
            return True

        return False
