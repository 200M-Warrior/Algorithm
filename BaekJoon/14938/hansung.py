import sys
INF=float('inf')
n, m, r=map(int, input().split())
# index 맞춰주고
items=[0]+list(map(int, input().split()))

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(r):
    a, b, c=map(int, input().split())
    # 초기값 갱신
    graph[a][b]=min(graph[a][b], c)
    graph[b][a]=min(graph[b][a], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i==j:
                graph[i][j]=0
            # 그냥 가는 것보다 거쳐서 가는게 이득인지
            graph[i][j]=min(graph[i][j], graph[i][k]+graph[k][j])

# 시작점이 없으니까 초기화
results=[0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        # 반복문 돌면서 방문 가능하다면 m보다 작거나 같다면
        if graph[i][j]<=m:
            # 방문한걸로 처리
            results[i]+=items[j]
print(max(results))