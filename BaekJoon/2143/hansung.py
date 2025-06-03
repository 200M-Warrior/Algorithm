from collections import Counter
import sys
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

A_subsum = []
for i in range(N):
    total = 0
    for j in range(i, N):
        total += A[j]
        A_subsum.append(total)

B_subsum = []
for i in range(M):
    total = 0
    for j in range(i, M):
        total += B[j]
        B_subsum.append(total)

# 빠른 탐색을 위해 Counter 로 고정 (한쪽도 될거 같음)
B_count = Counter(B_subsum)
A_count = Counter(A_subsum)

# A 부분합을 기준으로 T - a 가 B에 있는지 체크 해서 고정 개수 구함
cnt = 0
for a,num in A_count.most_common():
    cnt += B_count[T - a] * num

print(cnt)
