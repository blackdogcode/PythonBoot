import os
import art


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


print(art.logo)
print("Welcome to Secret Auction")

bidders = dict()

is_continue = True
while is_continue:
    name = input("What is your name?: ")
    price = int(input("How much price do you want to bid?: $"))
    bidders[name] = price

    response = input("More person to bid type 'yes' or 'no': ").lower()
    if response == 'no':
        is_continue = False
    else:
        clear()

win_bidder = [(name, price) for name, price in bidders.items() if max(bidders.values()) == price]
print("Win Bidder List")
for name, price in win_bidder:
    print(f"Name: {name}, Price: ${price}")