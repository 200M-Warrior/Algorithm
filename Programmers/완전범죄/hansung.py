def solution(info, n, m):
    from collections import deque

    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True  # 초기 상태 (0,0)

    for a_cost, b_cost in info:
        # 현재 단계에서 사용할 새로운 dp 테이블
        next_dp = [[False] * m for _ in range(n)]
        for a in range(n):
            for b in range(m):
                if dp[a][b]:
                    # A도둑이 훔치는 경우
                    if a + a_cost < n:
                        next_dp[a + a_cost][b] = True
                    # B도둑이 훔치는 경우
                    if b + b_cost < m:
                        next_dp[a][b + b_cost] = True
        dp = [row[:] for row in next_dp]

    # 가능한 dp 중 A의 흔적이 최소인 값 찾기
    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                return a
    return -1