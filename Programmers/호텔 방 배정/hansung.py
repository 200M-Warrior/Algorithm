import sys
# Recursion Error 방지- 재귀의 한도 10000까지 풀어주기
sys.setrecursionlimit(10000)

# 문제의 키는 중복의 경우 제일 작은 수를 얼마나 빨리 찾는지가 중요
# 현재 상태에서 얼마나 탐색을 빠르게 하느냐가 중요 -> 순회를 돌리면 10^12의 자연수를 모두 검색할 수 있을지
# 1번 간단한 순회 돌리기
  # 정확성 테스트 통과 26건, 효율성 테스트 전체
# 2번 범위 지정하기 : answer max를 기준으로 순회돌리기
  # 정확성 테스트 통과 26건, 효율성 테스트 전체
# 3번 이진 탐색 : 구현하다 실패..
# 4번 순차적으로 1을 더한다면 : 통과
# 소요 시간 -> 36분 소요

def solution(k, room_number):
    answer = []
    parent = {}
    def find(x):
        if x not in parent:
            return x
        parent[x] = find(parent[x])
        return parent[x]
    for num in room_number:
        res = find(num)
        answer.append(res)
        if res < k:
            parent[res] = res + 1
    return answer
