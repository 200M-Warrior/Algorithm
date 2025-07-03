# 오른쪽, 아래 방향만 존재
# 왼쪽 위부터 출발해 몇개 가능한지 세고, 갈 수 있는 것 업데이트

import sys
readline = sys.stdin.readline
from collections import defaultdict


def can_go(N, board, row, col, check_pos):
    for i in range(len(check_pos)):
        next_row, next_col = row + check_pos[i][0], col + check_pos[i][1]
        if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N or board[next_row][next_col] == 1:
            return False
    return True


N = int(readline())
board = [list(map(int, readline().split())) for _ in range(N)]


check_board = [
    [[[0, 1]], [[0, 1], [1, 0], [1, 1]]],  # 가로
    [[[1, 0]], [[0, 1], [1, 0], [1, 1]]],  # 세로
    [[[0, 1]], [[1, 0]], [[0, 1], [1, 0], [1, 1]]],  # 대각선
]

mvs = [
    [(0, 1), (1, 1)],  # 가로
    [(1, 0), (1, 1)],  # 세로
    [(0, 1), (1, 0), (1, 1)],  # 대각선
]

next_direction = [
    [0, 2],  # 가로 -> 가로, 대각선
    [1, 2],  # 세로 -> 세로, 대각선
    [0, 1, 2],  # 대각선 -> 가로, 세로, 대각선
]

count = [[defaultdict(int) for _ in range(N)] for _ in range(N)]
count[0][1][0] += 1  # direction, count


for row in range(N):
    for col in range(N):
        if count[row][col]:
            for direction, cur_count in count[row][col].items():            
                have_to_checks = check_board[direction]
                next_pos = mvs[direction]

                for i in range(len(have_to_checks)):
                    if can_go(N, board, row, col, have_to_checks[i]):
                        next_row, next_col = row + next_pos[i][0], col + next_pos[i][1]
                        count[next_row][next_col][next_direction[direction][i]] += cur_count


ans = sum(count[N - 1][N - 1].values())
print(ans)