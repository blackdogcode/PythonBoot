from card import *
import random


class Deck:

    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))

    def pop_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        ret = ""
        for idx, card in enumerate(self.cards, start=1):
            ret += str(card) + " "
            if idx % 13 == 0:
                ret += "\n"
        return ret

