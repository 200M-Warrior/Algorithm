import sys
input = sys.stdin.readline
size,pow = map(int,input().split())
mod = 1000
A = [list(map(int,input().split())) for _ in range(size)]

def mat_mul(A,B):
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j] % mod
                result[i][j] %= mod
    return result

def matrix_power(A, pow):
    if pow == 1:
        return [[i % mod for i in rows] for rows in A]
    is_odd = pow % 2
    result = [[(1 if i == j else 0) for j in range(size)] for i in range(size)]  # 단위 행렬 초기화
    while pow > 0:
        if pow % 2 == 1:
            result = mat_mul(result, A)
        A = mat_mul(A, A)
        pow //= 2
    # if is_odd:
    #     result = mat_mul(A,result)
    return result


result = matrix_power(A,pow)
for rows in result:
    print(*rows)