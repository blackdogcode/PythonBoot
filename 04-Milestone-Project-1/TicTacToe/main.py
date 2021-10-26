from collections import deque
import re


def display_board(board: list, size: int):
    # print head line
    print("   ", end="")
    for col_idx in range(size):
        print(f"| {col_idx} ", end="")
    print("")
    # print each row
    for row_idx, row in enumerate(board):
        print("-" * (5 * size))
        print(f" {row_idx} ", end="")
        for stone in row:
            print(f"| {stone} ", end="")
        print("")


def put_player_stone(board: list, size: int, player: str, stone: str):
    while True:
        position = input(f"Player {player}({stone}) turn. Please input your stone position <row,col>, e.g - 1,2: ")
        position = re.split(' |,', position)
        row, col = position
        if not row.isdigit() or not col.isdigit():
            print(f"Invalid: {row} or {col} is not number. Please try again.")
            continue

        row, col = int(row), int(col)
        if row >= size or col >= size:
            print(f"Invalid: {row} or {col} is out of board size. Please try again.")
        elif board[row][col] != " ":
            print(f"Invalid: There is a already stone in that position")
        else:
            board[row][col] = stone
            break


def win_check(board: list, size: int, color: str):
    # horizontal line
    for row in board:
        if row.count(color) == size:
            return True
    # vertical line
    cols = []
    for j in range(size):
        for i in range(size):
            cols.append(board[i][j])
        if cols.count(color) == size:
            return True
        cols.clear()
    # diagonal Line
    # left-top to right-bottom
    diagonal = []
    for i in range(size):
        diagonal.append(board[i][i])
    if diagonal.count(color) == size:
        return True
    diagonal.clear()
    # left-bottom to right-top
    i, j = size - 1, 0
    for _ in range(size):
        diagonal.append(board[i][j])
        i -= 1
        j += 1
    if diagonal.count(color) == size:
        return True

    return False


if __name__ == '__main__':
    # initialization
    board_size = 3
    board = [[' '] * board_size for i in range(board_size)]
    display_board(board, board_size)
    # start game
    player_stone = {"A": "○", "B": "●"}
    player_turn = deque(["A", "B"])
    for _ in range(board_size ** 2):
        player = player_turn.popleft()
        stone = player_stone[player]
        put_player_stone(board, board_size, player, stone)
        display_board(board, board_size)
        if win_check(board, board_size, stone):
            print(f'Player {player}({stone}) win!')
            break
        player_turn.append(player)
    else:
        print(f"The game is draw")
