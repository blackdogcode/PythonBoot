# 문제링크: https://www.acmicpc.net/problem/2178
from collections import deque

# 상하좌우 이동 상대좌표
dy = [-1, +0, +1, +0]
dx = [+0, +1, +0, -1]

height, width = map(int, input().split())

maps = []
for _ in range(height):
    row = input().strip()
    row = [int(num) for num in row]
    maps.append(row)

# 시작 점에서 각 정점까지 최단 거리
distance = [[-1] * width for _ in range(height)]

start_y, start_x = (0, 0)
distance[start_y][start_x] = 1  # 문제 조건: 시작위치도 거리 수에 포함

queue = deque()
queue.append((start_y, start_x))
while len(queue) != 0:
    here = queue.popleft()
    here_y, here_x = here

    for idx in range(len(dy)):
        there_y, there_x = here_y + dy[idx], here_x + dx[idx]
        # 1. 미로 범위를 벗어난 경우 무시
        if (there_y < 0 or there_y >= height) or (there_x < 0 or there_x >= width):
            continue
        # 2. 이동할 수 없는 칸의 경우 무시
        if maps[there_y][there_x] == 0:
            continue
        if distance[there_y][there_x] == -1:
            distance[there_y][there_x] = distance[here_y][here_x] + 1
            queue.append((there_y, there_x))

print(distance[height - 1][width - 1])