# https://games.washingtonpost.com/games/blackjack
# https://en.wikipedia.org/wiki/Blackjack
import random
import art

card_symbol = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_scores = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(cards: list) -> int:
    score = 0
    for card in cards:
        score += card_scores[card_symbol.index(card)]
    if score > 21 and 'A' in cards:
        for _ in range(cards.count('A')):
            score -= 10
            if not score > 21:
                break
    return score


print(art.logo)
print("Welcome to Blackjack!")

user_cards = []
dealer_cards = []

for _ in range(2):
    user_cards.append(random.choice(card_symbol))
    dealer_cards.append(random.choice(card_symbol))

print(f"Your Cards: {user_cards}")
print(f"Dealer Cards: {[dealer_cards[0], '']}")

user_score = calculate_score(user_cards)
dealer_score = calculate_score(dealer_cards)

is_end = False
while True:
    choice = input("Would you like to 'stand' or 'hit' the cards?: ")
    if choice == 'stand':
        break
    elif choice == 'hit':
        user_cards.append(random.choice(card_symbol))
    else:
        print("Invalid Command")
    print(user_cards)
    user_score = calculate_score(user_cards)
    if user_score > 21:
        print("You Bust! You Lose")
        is_end = True
        break

if not is_end:
    while dealer_score < 17:
        dealer_cards.append(random.choice(card_symbol))
        dealer_score = calculate_score(dealer_cards)
        if dealer_score > 21:
            is_end = True
            print("Dealer Bust! You Win")
        print(dealer_cards)

if not is_end:
    print(f"Your Score: {user_score} and Dealer Score: {dealer_score}")
    if user_score > dealer_score:
        print("You Win!")
    elif user_score < dealer_score:
        print("Dealer Win!")
    else:
        print("Draw")
