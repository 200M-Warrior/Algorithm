import sys
input = sys.stdin.readline
'''
두 지붕을 잇는 선분이 A와 B를 제외한 다른 고층 빌딩을 지나거나 접하지 않아야 한다. 가장 많은 고층 빌딩이 보이는 빌딩을 구하고, 거기서 보이는 빌딩의 수를

보인다의 기준 : A, B 사이에 다른 고층 빌딩을 지나거나 접하지 않아야 한다.
사실 상 2차 행렬이 필요한거 아님?
  1 5 3 2 6 3 2 6 4 2 5 7 3 1 5
1 0 0 
5
3
2
6
3
2
6
4
2
5
7
3
1
5
'''
def is_linked(x,y):
    global graph
    # x : (i,h)
    # y : (j,h)
    n = y[0] - x[0] # x 축 기울기
    icm = (y[1] - x[1])/ n # y축 기울기
    base_x1 = x[1]
    base_x0 = x[0]
    for k in range(1, n):
        cur_x1, cur_x0 = base_x1 + icm * k , base_x0 + k
        # print('cur_x1, cur_x0 icm*k k graph[cur_x0]',cur_x1, cur_x0, icm*k, k, graph[cur_x0])
        if graph[cur_x0] >= cur_x1:
                return False
    # print('*'*100)
    return True

# def main2(graph, N):
#     for i in range(5, N):
#         print('i, graph[i], is_linked((4,graph[4]), (i, graph[i]))',i, graph[i], is_linked((4,graph[4]), (i, graph[i])))

def main(graph,N):
    linked_dict = {i : set() for i in range(N)}
    for i in range(N):
        for j in range(i + 1, N): 
            if j not in linked_dict[i]:
                if is_linked((i,graph[i]), (j, graph[j])):
                    linked_dict[i].add(j)
                    linked_dict[j].add(i)
    # for key in linked_dict:
    #     print(f'{key} : {linked_dict[key]} so length : {len(linked_dict[key])}')
    return max([len(v) for v in linked_dict.values()])
        
if __name__ == "__main__":
    N = int(input())
    graph = list(map(int,input().split()))
    print(main(graph,N))
