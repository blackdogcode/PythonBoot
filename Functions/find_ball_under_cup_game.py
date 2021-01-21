from random import shuffle


def player_guess():
    pos = -1
    pos_list = [1, 2, 3]
    while True:
        pos = input('>: ')
        if pos == 'quit':
            exit(0)
        try:
            pos = int(pos)
            if pos in pos_list:
                break
            else:
                print(f'Invalid Position {pos}, choose among 1,2,3')
        except ValueError:
            print(f'Invalid Value: Please type integer value')
    return pos


def start_game():
    print("Welcome find a ball under cup game!\nIf you want to finish the game please type 'quit'")
    print('Guess the cup number(1,2,3), where the ball is')
    ball_in_cup = ['X', 'O', 'X']
    guess_pos = -1
    while True:
        shuffle(ball_in_cup)
        guess_pos = player_guess() - 1
        if guess_pos == ball_in_cup.index('O'):
            break
        else:
            print(f'Oops! There is no ball in {guess_pos + 1} cup')
    print('Congratulation, You find the ball!')


start_game()
