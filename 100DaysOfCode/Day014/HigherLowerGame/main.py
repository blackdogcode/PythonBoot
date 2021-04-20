import art
import data

import sys
import os
import random


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    print(art.logo)

    random.seed()
    game_score = 0
    while True:
        game_a = random.choice(data.games)
        game_b = random.choice(data.games)

        print(f'{game_a["title"]}')
        print(art.vs)
        print(f'{game_b["title"]}')

        choice = {'A': game_a, 'B': game_b}
        sel = input("Which one has more reviews? Type A or B\n--> ")
        user_choice = None;
        remain_one = None;
        if sel == 'A':
            user_choice = choice['A']
            remain_one = choice['B']
        else:
            user_choice = choice['B']
            remain_one = choice['A']

        if user_choice['reviews'] >= remain_one['reviews']:
            game_score += 1
        else:
            print(f'False, Game Score is {game_score}')
            sys.exit(0)
