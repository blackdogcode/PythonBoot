import random

if __name__ == "__main__":
    random.seed()

    head_tail = ['head', 'tail']
    coin_face = head_tail[random.randint(0, 1)]
    user_choice = input('Head or Tail?\n--> ').lower()
    while user_choice not in head_tail:
        print(f'Invalid Choice. Please try again')
        user_choice = input('Head or Tail?\n--> ').lower()

    if user_choice == coin_face:
        print(f'{coin_face.capitalize()}! You Win :)')
    else:
        print(f'{coin_face.capitalize()}! You Lose :(')
