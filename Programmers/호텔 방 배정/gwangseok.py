def solution(k, room_number):
    answer = []
    
    dp = {}
    
    for r in room_number:
        if r == k:
            answer.append(k)
            continue

        history = []
        while r in dp:
            history.append(r)
            r = dp[r]
            
        answer.append(r)
        for h in history:
            dp[h] = r + 1
        dp[r] = r + 1
    
    return answer

# def solution(k, room_number):
#     answer = []
    
#     dp = [i for i in range(k + 1)] -> 시간 초과 원인.
#     is_visited = [False] * (k + 1)
    
#     for r in room_number:
#         if r == k:
#             answer.append(k)
#             continue
#         history = []
#         while is_visited[r]:
#             history.append(r)
#             r = dp[r]
            
#         answer.append(r)
#         is_visited[r] = True
#         for h in history:
#             dp[h] = dp[r + 1]
#         dp[r] = dp[r + 1]
    
#     return answer