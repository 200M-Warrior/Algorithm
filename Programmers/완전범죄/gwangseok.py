def solution(info, n, m):
    # O(len(info))
    sum_a_footprints = sum([a_footprint for a_footprint, _ in info])

    # O(len(info) * m)
    dp = [[sum_a_footprints] * (m + 1) for _ in range(len(info))]

    for i in range(len(info)):
        a_footprint, b_footprint = info[i]
        for b_footprints_tolerance in range(1, m + 1):
            if b_footprints_tolerance <= b_footprint:
                dp[i][b_footprints_tolerance] = dp[i - 1][b_footprints_tolerance]
            else:
                dp[i][b_footprints_tolerance] = min(
                    dp[i - 1][b_footprints_tolerance],
                    dp[i - 1][b_footprints_tolerance - b_footprint] - a_footprint
                    # dp[i - 1][b_footprints_tolerance]에는 이미 1개의 여유가 있다.
                    # 따라서 b_footprints_tolerance - b_footprint - 1을 하지 않는다.
                )
    
    if dp[-1][-1] >= n:
        return -1
    return dp[-1][-1]