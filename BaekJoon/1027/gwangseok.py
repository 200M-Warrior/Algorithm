import sys
read_line = sys.stdin.readline


def search(buildings):
    results = [0] * len(buildings)
    for i in range(len(buildings)):
        max_slope = -float('inf')
        for j in range(i + 1, len(buildings)):
            slope = (buildings[j] - buildings[i]) / (j - i)
            if slope > max_slope:
                results[i] += 1
                max_slope = slope    
    return results


N = int(read_line())
buildings = list(map(int, read_line().split()))

right = search(buildings)
left = search(buildings[::-1])

answer = 0
for i in range(N):
    answer = max(answer, left[i] + right[N - i - 1])
print(answer)