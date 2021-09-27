# 로봇이 움직일수 있는 구역 모양은 좌표(0, 0)을 중심으로 마름모가 된다.
#
# 좌표에서 한 분면에 대해 좌우 및 대각선 대칭이므로 1사 분면만 계산하면 된다. 따라서 로봇이 이동 가능 경우는 (x+1, y)와 (x, y+1)만 고려한다.
#
# 1사분면에 대해 대칭이므로 1사분면의 안전한 영역을 계산 후 나머지 분면에 대해 곱하고 중복되는 좌표 축을 고려하여 빼준다.
#
# 코드로 구현하면 아래와 같다.
def digit_sum(num):
    num = str(abs(num))
    num_sum = 0
    for digit in num:
        num_sum += int(digit)
    return num_sum


def is_robot_safe(x, y, n):
    pos_sum = digit_sum(x) + digit_sum(y)
    return pos_sum <= n


def move_robot(x, y, n, grid):
    if x > n or y > n:
        return None

    if is_robot_safe(x, y, n):
        grid[x][y] = 1
    else:
        grid[x][y] = 0

    move_robot(x + 1, y, n, grid)
    move_robot(x, y + 1, n, grid)


if __name__ == '__main__':
    N = 3
    # map creation
    grid = []
    for i in range(N + 1):
        row = []
        for j in range(N + 1):
            row.append(-1)
        grid.append(row)

    # make robot moving around map
    move_robot(0, 0, N, grid)

    # area of safety points of map
    safe_area = 0
    for row in grid:
        safe_area += sum(row)
    safe_area = (safe_area * 4) - ((N + 1) * 4) + 1  # get rid of duplicated x,y axis
    print(safe_area)
