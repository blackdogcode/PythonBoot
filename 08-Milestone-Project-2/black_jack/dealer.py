from person import *


class Dealer(Person):

    def show_cards(self, hidden=False):
        if hidden:
            print("■  " + ' '.join(map(str, self.cards[1:])))
        else:
            print(' '.join(map(str, self.cards)))
