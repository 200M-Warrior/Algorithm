#!/bin/bash

# 순서가 정해진 작업을 차례로 수행 + 순서 결정 -> 위상 정렬

from collections import deque


def make_tree(n, edges):
    tree = [[] for _ in range(n)]
    parent = [None] * n

    q = deque([0])  # 0번 동굴에서 시작
    parent[0] = 0
    while q:
        root  = q.popleft()
        for child in edges[root]:
            if parent[child] is None:
                # 아직 부모가 정해지지 않았다면
                parent[child] = root
                tree[root].append(child)
                # root를 먼저 방문해야 child 방문 가능
                q.append(child)
    
    return tree


def cal_indegree(tree, order):
    indegree = [0] + [1] * (len(tree) - 1)    
    for before, after in order:
        indegree[after] += 1
        tree[before].append(after)  # 이후에 방문할 수 있기 때문에 가상의 간선 연결

    return indegree


def tolological_sort(tree, indegree):
    q = deque()
    for i in range(len(tree)):
        if indegree[i] == 0:
            q.append(i)

    sorted_order = []
    while q:
        node = q.popleft()
        sorted_order.append(node)
        for child in tree[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                q.append(child)

    return sorted_order


def solution(n, path, order):
    edges = [[] for _ in range(n)]

    # O(path)
    for pair in path:
        edges[pair[0]].append(pair[1])
        edges[pair[1]].append(pair[0])

    tree = make_tree(n, edges)


    indegree = cal_indegree(tree, order)
    max_visit_order = tolological_sort(tree, indegree)

    return len(max_visit_order) == n
    

cases = [
    (9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]),
    (9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]),
    (9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]])
]

for case in cases:
    # n     : 2이상 200,000이하
    # path  : n - 1
    # order : 1이상 n / 2이하
    print(solution(*case))
