class Card:
    suits = ("♠", "♡", "♣", "◇")
    ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": 11}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = Card.values[self.rank]

    def __str__(self):
        return f"{self.suit}{self.rank}"
