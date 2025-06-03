import sys
read_line = sys.stdin.readline
from collections import defaultdict


def get_subsums(arr):
    # O(N^2)
    sum_dict = defaultdict(int)
    for i in range(len(arr)):
        subsum = 0
        for j in range(i, len(arr)):
            subsum += arr[j]
            sum_dict[subsum] += 1
    
    return sum_dict


target = int(read_line())
n = int(read_line())
a = list(map(int, read_line().split()))
m = int(read_line())
b = list(map(int, read_line().split()))

sum_a = get_subsums(a)
sum_b = get_subsums(b)

count = 0
for k, v in sum_a.items():
    if (target - k) in sum_b:
        count += v * sum_b[target - k]
print(count)