import sys
read_line = sys.stdin.readline
from collections import deque

"""
아기 상어의 크기는 2이다.
큰 물고기 통과 못함.
같은 물고기 통과 가능 먹지 못함.
작은 물고기 통과 가능 먹음.

먹을 수 있는 물고기 x -> 엄마에게 도움 요청
먹을 수 있는 물고기 중 가장 가까운 물고기를 먹으러 간다.
거리가 같다면 가장 위에 있는 것. 그 중 가장 왼쪽에 있는 것을 먹음.

자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가한다.
몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구해라.
"""


N = int(read_line())
space = [list(map(int, read_line().split())) for _ in range(N)]

for shark_row in range(N):
    is_hit = False
    for shark_col in range(N):
        if space[shark_row][shark_col] == 9:
            space[shark_row][shark_col] = 0
            is_hit = True
            break
    if is_hit: break
del is_hit

shark = 2
mvs = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 상, 좌, 우, 하
q = deque([(shark_row, shark_col)])  # (row, col, 먹이, 시간)

cur_time = answer = 0
feed = shark

visited = [[False] * N for _ in range(N)]
visited[shark_row][shark_col] = True 

while q:
    next_candidates = []
    while q:
        cur_row, cur_col = q.popleft()

        for dr, dc in mvs:
            next_row, next_col = cur_row + dr, cur_col + dc
            if 0 <= next_row < N and 0 <= next_col < N and not visited[next_row][next_col]:
                if space[next_row][next_col] <= shark:
                    visited[next_row][next_col] = True
                    next_candidates.append((next_row, next_col))
    
    cur_time += 1
    next_candidates.sort()

    for next_row, next_col in next_candidates:
        if 0 < space[next_row][next_col] < shark:
            answer = cur_time
            space[next_row][next_col] = 0
            visited = [[False] * N for _ in range(N)]
            feed -= 1
            if feed == 0:
                shark += 1
                feed = shark
            q = deque([(next_row, next_col)])  # 큐 초기화
            break
    else:
        q = deque(next_candidates)

print(answer)