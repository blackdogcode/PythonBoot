import art

import sys
import random


def check_guess(chosen_number, guess_nubmer):
    if guess_nubmer == chosen_number:
        return True
    elif guess_number > chosen_number:
        print(f'Too high. Guess again.')
    else:
        print(f'Too low. Guess again.')
    return False


if __name__ == "__main__":
    print(art.logo)
    print(f'Welcome to the Number Guessing Game!')

    difficulty = {'easy': 10, 'hard': 5}
    difficulty_option = input('Choose a difficulty. Type "easy" or "hard"\n--> ')
    remain_try_count = difficulty[difficulty_option]

    random.seed()
    chosen_number = random.randint(1, 100)
    while remain_try_count > 0:
        print(f'You have {remain_try_count} attempts remaining to guess the number between 1 to 100')
        guess_number = int(input(f'Make a guess number: '))
        if guess_number < 0 or guess_number > 100:
            print(f'{guess_number} is out of range, 1-100, try again')
            continue
        if check_guess(chosen_number, guess_number):
            break
        else:
            remain_try_count -= 1
    else:
        sys.exit(f'Oops! There is no more remaining attempts\nThe number is {chosen_number}')
    print(f'Congratulation. The number is {chosen_number}')