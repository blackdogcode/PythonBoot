"""
What is War Card Game: https://en.wikipedia.org/wiki/War_(card_game)
"""
from deck import *
from player import *

if __name__ == '__main__':
    player_a_deck = Player()
    player_b_deck = Player()

    # The deck is divided evenly among the players
    deck = Deck()
    deck.shuffle()
    for _ in range(int(len(deck) / 2)):
        player_a_deck.add_card(deck.pop_card())
        player_b_deck.add_card(deck.pop_card())

    # War Card Game Start
    for round_count in range(1000):
        # check wining condition
        if len(player_a_deck) == 0:
            print("Player A out of cards!")
            print("Player B win the game!")
            break

        if len(player_b_deck) == 0:
            print("Player B out of cards!")
            print("Player A win the game!")
            break

        print(f"round {round_count}: ")

        # each player reveals the top card of their deck
        player_a_cards = [player_a_deck.pop_card()]
        player_b_cards = [player_b_deck.pop_card()]

        is_war = True
        while is_war:
            # the player with the higher card takes both of the cards played and moves them to their stack.
            if player_a_cards[-1].value > player_b_cards[-1].value:
                print(f"Player A win the round")
                player_a_deck.add_card(player_a_cards)
                player_a_deck.add_card(player_b_cards)
                is_war = False
            elif player_b_cards[-1].value > player_a_cards[-1].value:
                print(f"Player B win the round")
                player_b_deck.add_card(player_b_cards)
                player_b_deck.add_card(player_a_cards)
                is_war = False
            else:
                # if the two cards played are of equal value, then there is a "war".
                # both players place the next three cards face down and then another card face-up
                is_war = True
                print(f"WAR!")
                for _ in range(3):
                    # if a player runs out of cards during a war, player immediately loses
                    if len(player_a_deck) == 0:
                        is_war = False
                        break

                    if len(player_b_deck) == 0:
                        is_war = False
                        break

                    player_a_cards.append(player_a_deck.pop_card())
                    player_b_cards.append(player_b_deck.pop_card())
    else:
        print("Game is Draw")






