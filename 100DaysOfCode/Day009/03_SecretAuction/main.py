import art

if __name__ == "__main__":
    print(art.logo)
    print(f'Welcome to secret auction program')

    winner_name = input(f'What is your name? ')
    winner_bid = float(input(f"What's your bid? $"))
    bidders = {winner_name: winner_bid}
    while True:
        finish = False if input('Are there other bidders?\nType "yes" or "no"\n--> ') == 'yes' else True
        if finish: break

        name = input(f'What is her or his name? ')
        bid = float(input(f"What's {name} bid? $"))

        bidders[name] = bid
        if bid > winner_bid:
            winner_name = name
            winner_bid = bid

    print(f'The bid winner is {winner_name}\nThe bid price is ${winner_bid}')
