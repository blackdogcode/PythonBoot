# Tic Tac Toc Game : https://en.wikipedia.org/wiki/Tic-tac-toe

"""
[7 | 8 | 9]
[4 | 5 | 6]
[1 | 2 | 3]
"""
NUMPAD = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ROW = [2, 2, 2, 1, 1, 1, 0, 0, 0]
COL = [0, 1, 2, 0, 1, 2, 0, 1, 2]
SEL = set()


def display_game_info():
    print('-' * 100)
    print('Welcome to Tic Tac Toe Game')
    print('Tic Tac Toe is game for two players, X and O')
    print('Player succeeds in placing three of their marks in diagonal, horizontal, or vertical row is the winner!')
    print('-' * 100)


def create_player():
    while True:
        marks = ['O', 'X']
        player1_mark = input("Player1 Choose the mark 'O' or 'X': ")
        if player1_mark not in marks:
            print(f'Invalid Mark: {player1_mark} please insert valid mark')
        else:
            marks.remove(player1_mark)
            player2_mark = marks.pop()
            return player1_mark, player2_mark


def create_board():
    SEL.clear()
    return [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3']]


def display_board(board):
    for row in board:
        print('|', end=' ')
        for col in row:
            print(col, end=' | ')
        print('')


def mark_board(num, marker, board):
    if num not in NUMPAD:
        print('Please select between from 1 to 9 number')
        return -1
    elif num in SEL:
        print(f'{num} was already marked. Please select another number')
        return -1
    else:
        SEL.add(num)
        board[ROW[num-1]][COL[num-1]] = marker
        return 0


def check_win(num, board):
    i = ROW[num-1]
    j = COL[num-1]
    chk = []
    # horizontal line
    for marker in board[i]:
        chk.append(marker)
    if len(set(chk)) == 1: return True
    # vertical line
    chk.clear()
    for marker in board:
        chk.append(marker[j])
    if len(set(chk)) == 1: return True
    # diagonal line
    # 0. left-top to right-bottom
    chk.clear()
    chk = [board[0][0], board[1][1], board[2][2]]
    if len(set(chk)) == 1 and [i, j] in [[0, 0], [1, 1], [2, 2]]: return True
    # 1. right-top to left-bottom
    chk.clear()
    chk = [board[0][2], board[1][1], board[2][0]]
    if len(set(chk)) == 1 and [i, j] in [[0, 2], [1, 1], [2, 0]]: return True

    return False


if __name__ == '__main__':
    display_game_info()
    game_board = create_board()
    player1_mark, player2_mark = create_player()
    display_board(game_board)

    player_turn = True
    while True:
        if len(SEL) == len(NUMPAD):
            print('Draw Game') 
            break

        player1_num = None
        player2_num = None
        try:
            if player_turn:
                player1_num = int(input('Player1 Choice: '))
                mark_board(player1_num, player1_mark, game_board)
                display_board(game_board)
                if check_win(player1_num, game_board):
                    print('Player1 Win!')
                    break
            else:
                player2_num = int(input('Player2 Choice: '))
                mark_board(player2_num, player2_mark, game_board)
                display_board(game_board)
                if check_win(player2_num, game_board):
                    print('Player2 Win!')
                    break
            player_turn = not player_turn
        except ValueError:
            print('Please type numeric number')