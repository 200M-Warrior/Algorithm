from collections import deque

def bfs(n, graph, order):
    visited = [False] * n
    visited[0] = True

    locked = [False] * n
    order_dict = {A: B for A, B in order}
    for A, B in order:
        locked[B] = True
        if B == 0 : return False
    
    queue = deque()
    queue.append(0)
    waits = set()

    while queue:
        node = queue.popleft()

        # unlock 조건
        if node in order_dict:
            next_node = order_dict[node]
            locked[next_node] = False  # 잠금 해제!

            if next_node in waits:
                waits.remove(next_node)
                visited[next_node] = True
                queue.append(next_node)

        for next_node in graph[node]:
            if visited[next_node]:
                continue

            if locked[next_node]:
                waits.add(next_node)
                continue

            visited[next_node] = True
            queue.append(next_node)

    return all(visited)

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    return bfs(n, graph, order)