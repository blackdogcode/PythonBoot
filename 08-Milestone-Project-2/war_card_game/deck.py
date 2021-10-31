from card import *


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.cards.append(Card(suit, rank))

    def pop_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            print("deck is empty")
            return 0

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"There is {len(self)} cards in the deck"
