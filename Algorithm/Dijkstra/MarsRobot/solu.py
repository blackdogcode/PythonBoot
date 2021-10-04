import heapq

dy = [-1, +0, +1, +0]
dx = [+0, +1, +0, -1]

INF = 987654321

def solution(maps, c):
    # 로봇의 현재 위치와 도착해야할 목적지 좌표를 찾는다
    start_x, start_y = None, None
    end_x, end_y = None, None
    for j, row in enumerate(maps):
        if 2 in row:
            start_y, start_x = j, row.index(2)
        if 3 in row:
            end_y, end_x = j, row.index(3)
            maps[end_y][end_x] = 0

    # 다익스트라 알고리즘으로 최단경로를 구한다
    height, width = len(maps), len(maps[0])
    distance = [[INF] * width for _ in range(height)]
    distance[start_y][start_x] = 0

    min_heap = []
    heapq.heappush(min_heap, (0, (start_y, start_x)))
    while len(min_heap) > 0:
        dist, (here_y, here_x) = heapq.heappop(min_heap)
        if distance[here_y][here_x] < dist:
            continue
        # 인접한 정점들의 최소 경로를 계산한다
        for idx in range(len(dy)):
            there_y, there_x = here_y + dy[idx], here_x + dx[idx]
            # 지도 범위 밖을 벗어나는 경우 무시 예외 처리
            if (there_y < 0 or there_y >= height) or (there_x < 0 or there_x >= width):
                continue
            # 인접 경로 계산하여 더 짧은 경로 인지 판단
            next_dist = 0
            if maps[there_y][there_x] == 1:  # 장애물
                next_dist = dist + c + 1
            else:
                next_dist = dist + 1
            if distance[there_y][there_x] > next_dist:
                distance[there_y][there_x] = next_dist
                heapq.heappush(min_heap, (next_dist, (there_y, there_x)))

    return distance[end_y][end_x]

with open('test_input.txt', 'r') as input_file:
    test_case = int(input_file.readline())
    for _ in range(test_case):
        cost = int(input_file.readline())
        height, width = map(int, input_file.readline().split())
        maps = []
        for _ in range(height):
            row = list(map(int, input_file.readline().split()))
            maps.append(row)

        result = solution(maps, cost)
        print(result)
