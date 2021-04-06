# https://getemoji.com/
# Python program to print Emojis: https://t.ly/kBgu

def draw_map(map):
    for i in range(0, len(map)+1):
        for j in range(0, len(map)+1):
            if i == 0:
                if j == 0:
                    print(f' ', end='')
                else:
                    print(f'   {j}', end='')
            else:
                if j == 0:
                    print(f'{i}', end='')
                else:
                    print(f'  {map[i-1][j-1]}', end='')
        print()


if __name__ == "__main__":
    row1 = ['\U0001F3D8', '\U0001F3D8', '\U0001F3D8']
    row2 = ['\U0001F3D8', '\U0001F3D8', '\U0001F3D8']
    row3 = ['\U0001F3D8', '\U0001F3D8', '\U0001F3D8']
    map = [row1, row2, row3]

    draw_map(map)

    # get coordinate
    position = int(input('Where do you want to attack by rocket?\n--> '))
    row = int(position / 10)
    col = int(position % 10)
    map[row-1][col-1] = '\U0001F680'

    draw_map(map)