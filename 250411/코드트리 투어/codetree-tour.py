import heapq
import sys
input = sys.stdin.readline

Q = int(input())
pp = set()
earning = [-1]*(30_001)
destination = [-1]*(30_001)
start = 0
dijkstra_result = {0: []}
cost_result = {0: []}


def dijkstra(start, graph, n, pp):
    dist = [float('inf')] * (n)
    dist[start] = 0
    hq = [(0, start)]  # (거리, 노드)

    while hq:
        cur_dist, cur_node = heapq.heappop(hq)

        if dist[cur_node] < cur_dist:
            continue

        for next_node, weight in graph[cur_node]:
            cost = cur_dist + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(hq, (cost, next_node))

    return dist

def make_graph(n, edges):
    graph =[[] for _ in range(n)]
    for edge in edges:
        v, u, w = edge
        graph[v].append((w, u))
        graph[w].append((v, u))
    return graph

for i in range(Q):
    #print(pp)
    cmd = list(map(int, input().split()))
    op = cmd[1:]
    if cmd[0] == 100:
        n, m = op[0], op[1]
        edge = op[2:]
        edges = []
        for i in range(0, m*3, 3):
            u, w, v= edge[i], edge[i+1], edge[i+2]
            edges.append((u, v, w))
        graph = make_graph(n,edges)
        dijkstra_result[start] = dijkstra(start, graph, n, pp)



    if cmd[0] == 200:
        id, revenue, dest = op[0], op[1], op[2]
        earning[id] = revenue
        destination[id] = dest
        pp.add(id)
        cost = dijkstra_result[start][dest]
        if revenue - cost >= 0:
            heapq.heappush(cost_result[start], (-1*(revenue - cost), id)) #최대를 찾아야 해서 -
        else:
            heapq.heappush(cost_result[start], (1, id))

    if cmd[0] == 300:
        id = op[0]
        if id in list(pp):
            earning[id] = -1
            destination[id] = -1
            pp.remove(id)

    if cmd[0] == 400:
        if not cost_result[start]:
            print(-1)
        else:
            while cost_result[start]:
                revenue, id = heapq.heappop(cost_result[start])
                #print(start, revenue, id)
                if id in pp:
                    if revenue >= 1 :
                        print(-1)
                    else:
                        print(id)
                        pp.remove(id)  # 중복 추천 방지
                    break
            else:
                print(-1)



    if cmd[0] == 500:
        start = op[0]
        if start not in cost_result:
            cost_result[start] = []

        if start not in dijkstra_result:
            dijkstra_result[start] = dijkstra(start, graph, n, pp)

        for id in pp:
            revenue = earning[id]
            dest =destination[id]
            cost = dijkstra_result[start][dest]

            if revenue - cost >= 0:
                heapq.heappush(cost_result[start], (-1 * (revenue - cost), id))  # 최대를 찾아야 해서 -
            else:
                heapq.heappush(cost_result[start], (1, id))
        #여행 상품 생성

