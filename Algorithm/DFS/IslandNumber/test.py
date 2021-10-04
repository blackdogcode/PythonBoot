# 움직일 수 있는 상대 좌표: 상하좌우 및 대각선
dx = [+0, +1, +1, +1, +0, -1, -1, -1]
dy = [-1, -1, +0, +1, +1, +1, +0, -1]


def dfs(y, x, maps, w, h):
    # 이미 방문한 점인지 체크
    if maps[y][x] == 0:
        return None

    # 해당 점을 방문한 것으로 체크
    maps[y][x] = 0

    for idx in range(len(dx)):
        y, x = y + dy[idx], x + dx[idx]
        # 1. 이동하려는 위치가 지도밖을 벗어나지 않는 지 체크
        # 2. 이동하려는 위치가 연결된 지점인지 확인
        if (0 <= y < h) and (0 <= x < w) and (maps[y][x] == 1):
            dfs(y, x, maps, w, h)
        y, x = y - dy[idx], x - dx[idx]


with open('test.txt', 'r') as input_file:
    result = []
    while True:
        w, h = map(int, input_file.readline().split())
        # 테스트 케이스 종료 조건
        if w == 0 and h == 0:
            break
        maps = []
        for _ in range(h):
            maps.append(list(map(int, input_file.readline().split())))

        island_count = 0
        for y in range(h):
            for x in range(w):
                if maps[y][x] == 1:
                    dfs(y, x, maps, w, h)
                    island_count += 1
        result.append(island_count)

    for ret in result:
        print(ret)
