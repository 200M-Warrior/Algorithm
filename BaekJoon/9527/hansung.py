'''
누적합으로 풀려했는데
오히려 그게 메모리 잡아먹는 거 같아서
고민을 해보다가

자리수 별로 세는 걸 생각해봄
'''
import sys
input = sys.stdin.readline

S, E = map(int, input().split())

def count_ones_up_to(n):
    count = 0
    i = 0
    while (1 << i) <= n:
        # step 
        step_length = 1 << (i + 1)
        cur_step = n // step_length
        count += cur_step * (1 << i)

        # 이게 되게 어려웠음
        # 현재 스텝에서 step_length까지 가고
        # 거기서 나머지 가지 몬한 것에서 반복되는 경우 만큼 제외했을 때 
        # 예를 들어 step_length 가 4이면 나머지는 최대 3인데 이게 (1<<i)는 2라는 거니까 해당 범위에서 얼마나 갈 수 있는지  
        left_step = n % step_length
        count += max(0, left_step - (1 << i) + 1)

        i += 1
    return count

# f(E) - f(S-1)
ans = count_ones_up_to(E) - count_ones_up_to(S - 1)
print(ans)

'''
12 라고 가정하면
i는 총 0,1,2,3 까지 반복
2^(k+1)에서 2^(k)만큼 1이 반복됨


1의 자리 부터 반복되는 횟수를 계산

i == 0 일때 -> 비트자리수가 0임을 가정 
cur_step == 6 * (2^0) 6
left_step == 12 % 2== 0 -2 + 1 -1 0

i == 1 일때 -> 비트자리수가 1임을 가정 (10 ~ 11)
cur_step == 3 * (2^1) 6
left_step == 12 % 4 == 0 - 2 + 1 -1 0

i == 1 일때 -> 비트자리수가 1임을 가정 (10 ~ 11)
cur_step == 3 * (2^1) 6
left_step == 12 % 4 == 0 - 2 + 1 -1 0
'''