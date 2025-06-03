import sys
from collections import deque

input = sys.stdin.readline

# 방향: 위, 왼, 아래, 오른
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(start):
    visited = [[-1] * N for _ in range(N)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 0

    fishes = []
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1 and graph[nx][ny] <= shark_size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

                    # 먹을 수 있는 물고기면 후보에 추가
                    if 0 < graph[nx][ny] < shark_size:
                        fishes.append((visited[nx][ny], nx, ny))

    # 거리, 위쪽, 왼쪽 순으로 정렬
    fishes.sort()
    return fishes

def solution():
    global shark_size
    x, y = shark_pos
    time = 0
    eat_count = 0

    while True:
        targets = bfs((x, y))
        if not targets:
            break

        dist, nx, ny = targets[0]
        time += dist
        eat_count += 1
        graph[x][y] = 0
        graph[nx][ny] = 0
        x, y = nx, ny

        if eat_count == shark_size:
            shark_size += 1
            eat_count = 0

    return time


# ====== 입력 ======
N = int(input())
graph = []
shark_size = 2

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 9:
            shark_pos = (i, j)
            row[j] = 0  # 아기 상어 초기 위치는 비워둔다
    graph.append(row)

print(solution())