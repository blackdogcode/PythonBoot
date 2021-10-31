from deck import *
from player import *
from dealer import *


if __name__ == '__main__':
    player = Player(balance=5000)
    dealer = Dealer()

    while True:
        if input("do you want to play blackjack?(y/n): ").lower() != 'y':
            print("Good Bye!")
            break

        player.clear_cards()
        dealer.clear_cards()

        deck = Deck()
        deck.shuffle()

        for _ in range(2):
            player.add_card(deck.pop_card())
            dealer.add_card(deck.pop_card())
        player.show_cards()
        dealer.show_cards(hidden=True)

        # black jack condition
        if player.total() == 21:
            print(f"Blackjack, You Win!")
            continue

        # player turn
        player_bust = False
        while True:
            choice = input("hit(h) or stay(s)?: ").lower()
            if choice != "s" and choice != "h":
                print(f"Invalid Command: {choice}. Please Try Again")
                continue
            if choice == "s":
                break
            if choice == "h":
                player.add_card(deck.pop_card())
                player.show_cards()
                if player.total() > 21:
                    player_bust = True
                    break
        if player_bust:
            print("You are Busted! Dealer Win!")
            continue

        # dealer turn
        print("-------------------------")
        print("Dealer Cards", end=" ")
        dealer.show_cards()
        print("-------------------------")

        while dealer.total() < 17:
            dealer.add_card(deck.pop_card())
            dealer.show_cards()

        if dealer.total() > 21:
            print("Dealer is Busted! You Win!")
            continue

        print("-------------------------")
        print("----Final Card Result----")
        print("Player Cards", end=" ")
        player.show_cards()
        print("Dealer Cards", end=" ")
        dealer.show_cards()
        print("-------------------------")
        if player.total() > dealer.total():
            print(f"Player Win")
        elif player.total() < dealer.total():
            print(f"Dealer Win")
        else:
            print(f"Game is Push")
