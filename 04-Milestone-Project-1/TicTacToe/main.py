from collections import deque
import re


def display_board(board, size):
    print("   ", end="")
    for i in range(size):
        print(f"| {i} ", end="")
    else:
        print("")

    for i, row in enumerate(board):
        print("---------------")
        print(f" {i} ", end="")
        for k in row:
            print(f"| {k} ", end="")
        else:
            print("")


def input_player_position(player, color, size):
    while True:
        player_position = input(f"Your turn {player}, {color}. Please input your position(e.g. 1,2): ")
        player_position = re.split(' |,', player_position)
        print(player_position)
        row, col = player_position
        if not row.isdigit() or not col.isdigit():
            print(f"{row} or {col} is not number: Please try again.")
        elif int(row) > 2 or int(col) > 2:
            print("The number is out of range. Please try again.")
        else:
            break

    return int(row), int(col)


def win_check(board: list, size: int, color: str):
    # horizontal line
    for row in board:
        if row.count(color) == size:
            return True
    # Vertical line
    cols = []
    for j in range(size):
        for i in range(size):
            cols.append(board[i][j])
        if cols.count(color) == size:
            return True
        else:
            cols.clear()
    # Diagonal Line
    # Left-Top to Right-Bottom
    diagonal = []
    for i in range(size):
        diagonal.append(board[i][i])
    if diagonal.count(color) == size:
        return True
    else:
        diagonal.clear()
    # Left-Bottom to Right-Top
    i, j = 2, 0
    for _ in range(3):
        diagonal.append(board[i][j])
        i -= 1
        j += 1
    if diagonal.count(color) == size:
        return True
    else:
        diagonal.clear()

    return False


if __name__ == '__main__':
    # initialization
    size = 3
    board = [[' '] * size for i in range(size)]
    display_board(board, size)

    player_color = {"A": "○", "B": "●"}
    player_turn = deque(["A", "B"])
    count = 0
    while True:
        if count == (size ** 2):
            print(f"Game is Draw")
            break
        player = player_turn.popleft()
        color = player_color[player]
        row, col = input_player_position(player, color, size)
        board[row][col] = color
        display_board(board, size)
        if win_check(board, size, color):
            print(f'Player {player}, {color} win!')
            break
        player_turn.append(player)
        count += 1
