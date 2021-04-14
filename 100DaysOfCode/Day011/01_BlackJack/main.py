# Black Jack Rule: https://en.wikipedia.org/wiki/Blackjack
# Black Jack Site: https://games.washingtonpost.com/games/blackjack/
import art

import os
import sys
import random
from emoji import emojize


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


ace = 11
ten = 10
blackjack = 21
deck = [2, 3, 4, 5, 6, 7, 8, 8, 10, 10, 10, 10, 11] # 11 for ACE


def cards_score(cards):
    sorted_cards = cards.copy()
    sorted_cards.sort()
    total_sum = sum(sorted_cards)
    if total_sum > blackjack:
        if ace in sorted_cards:
            j = sorted_cards.index(ace)
            for i in range(j, len(sorted_cards)):
                total_sum -= 10
                if total_sum <= blackjack:
                    break
    return total_sum


if __name__ == "__main__":
    print(art.logo)
    start = input('Do you want to play a game of Blackjack? Type "y" or "n": ')
    if start != 'y':
        print('Good Bye', emojize(":waving_hand:"))
        sys.exit(0)
    clear()

    random.seed()
    player_cards = []
    dealer_cards = []
    for i in range(2):
        player_cards.append(random.choice(deck))
        dealer_cards.append(random.choice(deck))
    player_score = cards_score(player_cards)
    dealer_score = cards_score(dealer_cards)

    print(f"Your cards {player_cards}, current score: {player_score}")
    print(f"Dealer's first cards: {dealer_cards[0]}")

    # player turn
    while player_score < 21:
        player_turn = input("Type 'y' to get another card, type 'n' to pass: ")
        if player_turn != 'y':
            break
        player_cards.append(random.choice(deck))
        player_score = cards_score(player_cards)
        print(f"Your cards {player_cards}, current score: {player_score}")

    # dealer turn
    while dealer_score < 17:
        dealer_cards.append(random.choice(deck))
        dealer_score = cards_score(dealer_cards)

    # game result
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    if player_score > 21:
        # If the player exceeds a sum of 21 ("busts"), the player loses, even if the dealer also exceeds 21.
        print('You Busts', emojize(":crying_face:"))
    elif dealer_score > 21:
        # If the dealer exceeds 21 ("busts") and the player does not, the player wins.
        print('You win', emojize(":grinning_face_with_smiling_eyes:"))
    elif player_score > dealer_score:
        # If the player attains a final sum higher than the dealer and does not bust, the player wins.
        print('You win', emojize(":grinning_face_with_smiling_eyes:"))
    elif player_score == dealer_score:
        if player_score == blackjack:
            # If the player is dealt an Ace and a ten-value card (called a "blackjack" or "natural")
            # and the dealer does not, the player wins and usually receives a bonus.
            if ace in player_cards and ten in player_cards:
                if ace in dealer_cards and ten in dealer_cards:
                    print('Push', emojize(":neutral_face:"))
                else:
                    print('You win with a Blackjack', emojize(":grinning_squinting_face:"))
            else:
                if player_score == dealer_score:
                    # If both dealer and player receive a blackjack no one wins.
                    print('Push', emojize(":neutral_face:"))
                else:
                    print('You win', emojize(":grinning_face_with_smiling_eyes:"))
        else:
            # If both dealer and player receive any other hands with the same sum called a "push", no one wins.
            print('Push', emojize(":neutral_face:"))
    else:
        if dealer_score == blackjack:
            print('Lose, dealer has Blackjack', emojize(":face_screaming_in_fear:"))
        else:
            print('You lose', emojize(":loudly_crying_face:"))
