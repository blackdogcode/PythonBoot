class Player:
    def __init__(self):
        self.cards = []

    def add_card(self, cards):
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)

    def pop_card(self):
        try:
            return self.cards.pop(0)
        except IndexError:
            print("Player don't have any cards")
            return 0

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return f"Player has {len(self)} cards"

