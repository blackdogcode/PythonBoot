def dfs(i, j, maps):
    if (i < 0 or i >= len(maps)) or (j < 0 or j >= len(maps[0])) or maps[i][j] == -1 or maps[i][j] == 0:
        return 0

    length = 0
    if i == 0 or maps[i - 1][j] == 0:
        length += 1
    if i == len(maps) - 1 or maps[i + 1][j] == 0:
        length += 1
    if j == 0 or maps[i][j - 1] == 0:
        length += 1
    if j == len(maps[0]) - 1 or maps[i][j + 1] == 0:
        length += 1

    maps[i][j] = -1
    length += dfs(i - 1, j, maps)
    length += dfs(i + 1, j, maps)
    length += dfs(i, j - 1, maps)
    length += dfs(i, j + 1, maps)
    return length


def solution():
    with open('test.txt', 'r') as input_file:
        test_case = int(input_file.readline())
        for _ in range(test_case):
            rows = int(input_file.readline())
            maps = []
            for _ in range(rows):
                maps.append(list(map(int, input_file.readline().split())))
        print(maps)
        if not maps:
            return 0

        max_island_length = 0
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == 1:
                    island_length = dfs(i, j, maps)
                    if island_length > max_island_length:
                        max_island_length = island_length
        return max_island_length


print(solution())
