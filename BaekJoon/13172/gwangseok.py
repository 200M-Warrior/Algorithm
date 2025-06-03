import sys
read_line = sys.stdin.readline
import math


def mod_func(a, b):
    if b == 1:
        return a
    elif b % 2 == 1:
        return a * mod_func(a, b - 1) % mod_num
    else:
        half = mod_func(a, b // 2)
        return half * half % mod_num
    

mod_num = 1000000007
ans = 0

for _ in range(int(read_line())):
    n, s = map(int, read_line().split())  # n: 주사위면 개수, s: 주사위의 면의 합
    g = math.gcd(n, s)
    n //= g
    s //= g
    ans += s * mod_func(n, mod_num-2) % mod_num
    ans %= mod_num

print(ans)