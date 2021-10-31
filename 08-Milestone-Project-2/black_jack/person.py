from card import *


class Person:

    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def total(self):
        values = []
        for card in self.cards:
            values.append(card.value)
        score = sum(values)
        while 13 in values and score > 21:
            score -= 10
            values.remove(13)
        return score

    def clear_cards(self):
        self.cards.clear()
