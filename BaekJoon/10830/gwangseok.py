import sys
read_line = sys.stdin.readline


def matrix_mult(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += (A[i][k] * B[k][j]) % 1000
                result[i][j] %= 1000
    return result


def matrix_pow(matrix, pow):
    if pow == 1:
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                matrix[r][c] %= 1000
        return matrix
    
    matrix_half_pow = matrix_pow(matrix, pow // 2)
    result = matrix_mult(matrix_half_pow, matrix_half_pow)

    if pow % 2:
        result = matrix_mult(result, matrix)
    
    return result



N, M = map(int, read_line().split())
matrix = [list(map(int, read_line().split())) for _ in range(N)]
for matrix_row in matrix_pow(matrix, M):
    print(*matrix_row)