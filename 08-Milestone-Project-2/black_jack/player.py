from person import *


class Player(Person):
    def __init__(self, balance=1000):
        super().__init__()
        self.balance = balance

    def show_cards(self):
        print(' '.join(map(str, self.cards)))
