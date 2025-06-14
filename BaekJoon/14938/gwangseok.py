import sys
read_line = sys.stdin.readline

import heapq


def dijkstra(root):
    dists = [2000] * (n + 1)
    queue = [(0, root)]  # (cost node)
    dists[root] = 0
    while queue:
        cost, node = heapq.heappop(queue)
        for next_node, next_cost in graph[node]:
            new_cost = cost + next_cost
            if new_cost < dists[next_node]:
                dists[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))
    
    ret = 0
    for node in range(1, n + 1):
        if dists[node] <= m:
            ret += items[node - 1]
    
    return ret


n, m, r = map(int, read_line().split())
items = list(map(int, read_line().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(r):
    node_a, node_b, cost = map(int, read_line().split())
    graph[node_a].append((node_b, cost))
    graph[node_b].append((node_a, cost))

answer = 0
for start_node in range(1, n + 1):
    answer = max(answer, dijkstra(start_node))

print(answer)