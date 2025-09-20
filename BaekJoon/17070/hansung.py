'''
사전에 정할고 다 하면 BFS로 풀수 있는거 아닌가?

1. BFS로 풀어봄 -> 64% 시간초과
2. 아무래도 중복이 좀 걸리는 듯 3차원 visited 추가
'''
import sys
from collections import deque
input = sys.stdin.readline

n_directions = [
    [[(0,1),(0,1)], [(0,1),(1,1)]], # 가로
    [[(1,0),(1,0)],[(1,0),(1,1)]], # 세로
    [[(1,1),(0,1)],[(1,1),(1,0)],[(1,1),(1,1)]] # 대각선
]
check_pos = [
    [[(0,1)], [(0,1),(1,0),(1,1)]], # 가로
    [[(1,0)],[(0,1),(1,0),(1,1)]],  # 세로
    [[(0,1)],[(1,0)],[(0,1),(1,0),(1,1)]] # 대각선
]

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

def get_position(idx1, idx2):
    if idx1[0] == idx2[0]: # 가로
        return 0
    if idx1[1] == idx2[1]: # 세로
        return 1
    return 2 # 대각선

def bfs():
    idx1, idx2 = (0,0), (0,1)
    queue = deque()
    queue.append((idx1, idx2, 0))
    
    visited = [[[0]*3 for _ in range(N)] for _ in range(N)]
    visited[idx2[0]][idx2[1]][0] = 1  # 시작 파이프 위치 (0,1), 가로 방향

    while queue:
        cur1, cur2, pos = queue.popleft()

        if cur2 == (N-1,N-1):
            continue

        for i, (n_dir, n_pos) in enumerate(zip(n_directions[pos], check_pos[pos])):
            n_idx1 = (cur1[0] + n_dir[0][0], cur1[1] + n_dir[0][1])
            n_idx2 = (cur2[0] + n_dir[1][0], cur2[1] + n_dir[1][1])

            check = [(cur2[0] + ch_idx[0], cur2[1] + ch_idx[1]) for ch_idx in n_pos]
            if 0 <= n_idx2[0] < N and 0 <= n_idx2[1] < N and all(graph[i][j] == 0 for i,j in check):
                next_pos = get_position(n_idx1, n_idx2)

                if visited[n_idx2[0]][n_idx2[1]][next_pos] == visited[cur2[0]][cur2[1]][pos]:
                    queue.append((n_idx1, n_idx2, next_pos))
                elif visited[n_idx2[0]][n_idx2[1]][next_pos] == 0:
                    queue.append((n_idx1, n_idx2, next_pos))

                visited[n_idx2[0]][n_idx2[1]][next_pos] += visited[cur2[0]][cur2[1]][pos]

    return sum(visited[N-1][N-1])

print(bfs())