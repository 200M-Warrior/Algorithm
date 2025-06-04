#!/bin/python3

# 참고 풀이: https://degurii.tistory.com/158

import sys
read_line = sys.stdin.readline

def get_sum(str_bin, cnt):
    if len(str_bin) == 1:
        return cnt + int(str_bin[0])

    if str_bin[0] == '1':
        border = '1' + '0' * (len(str_bin) - 1)  # 제일 앞이 1이고 나머지가 0인 이진수  : 1000...0
        cnt += cum_sums[len(str_bin) - 2]  # border보다 작은 이진수의 1의 개수 합       : 1 ~ 0111...1  
        cnt += (int(str_bin, 2) - int(border, 2) + 1)  # 제일 파이 1인 수의 개수       : 현재 수 - (border - 1) 만큼 있음.

    cnt = get_sum(str_bin[1:], cnt)  # Reursive하게 위에서 구한 것 나머지의 1의 개수를 구함.

    return cnt


cum_sums = [1]
max_digits = 55

for digit in range(1, max_digits):
    cum_sum = 2 * cum_sums[digit - 1] + 2 ** digit
    # 2 * cum_sums[digit - 1]   : 이전 것 + 이전 것 반복.
    # 2 ** digit                : 현재 자리수의 1의 개수
    cum_sums.append(cum_sum)

A, B = map(int, read_line().split()) # B가 항상 더 크거나 같은 수
print(get_sum(bin(B)[2:], 0) - get_sum(bin(A - 1)[2:], 0))  # B의 누적합에서 A-1의 누적합을 빼면 A부터 B까지의 1의 개수