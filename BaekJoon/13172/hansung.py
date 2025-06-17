import sys
import math
input = sys.stdin.readline
X = 1000000007
N = int(input())


total = 0
def solution(a,b):
    if b == 1:
        return a
    elif b % 2 == 1:
        return a * solution(a,b-1) % X
    else:
        half = solution(a,b//2)
        return half * half % X


for _ in range(N):
    N_i, S_i = map(int,input().split())
    gcd = math.gcd(N_i, S_i)
    N_i, S_i = N_i // gcd, S_i // gcd 

    total += S_i * solution(N_i,X-2)
    total %= X

print(total)