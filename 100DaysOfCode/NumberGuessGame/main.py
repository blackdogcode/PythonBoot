import random
import art

EASY_LEVEL_ATTEMPT = 15
HARD_LEVEL_ATTEMPT = 7


def check_answer(answer_number, guessed_number):
    if answer_number == guessed_number:
        return '='
    elif answer_number > guessed_number:
        return '>'
    else:
        return '<'


print(art.logo)
print("Welcome to the Number Guess Game!")
while True:
    correct_number = random.randint(1, 100)
    response_level = input("Select level Type 'EASY' or 'HARD': ").lower()

    if response_level == "easy":
        remain_attempts = EASY_LEVEL_ATTEMPT
    else:
        remain_attempts = HARD_LEVEL_ATTEMPT

    while remain_attempts > 0:
        guess_number = int(input("Guess a number between 1 and 100: "))
        result = check_answer(correct_number, guess_number)
        if result == '=':
            print("Congratulations! You Win!")
            break
        elif result == '>':
            print("Too Low")
        else:
            print("Too High")
        remain_attempts -= 1
        print(f"You have remain attempts: {remain_attempts}")
    if remain_attempts == 0:
        print(f"You Lose! The number is {correct_number}")

    response_continue_play = input("Do you want to play again? 'y' or 'n': ")
    if response_continue_play == "y":
        continue
    else:
        break
