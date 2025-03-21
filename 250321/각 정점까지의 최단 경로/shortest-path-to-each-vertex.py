import heapq

n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]

for i in range(m):
    s, e, v = edges[i]
    graph[s-1].append((e-1, v))
    graph[e-1].append((s-1, v))

def dijkstar(graph, source):
    pq = []
    heapq.heappush(pq, (0, source))
    dist = [float('inf')]*n
    dist[source] = 0
    
    while pq:
        min_dist, min_idx = heapq.heappop(pq)
        if min_dist != dist[min_idx]:
            continue
        
        for target_index, target_dist in graph[min_idx]:
            new_dist = dist[min_idx] + target_dist
            if dist[target_index] > new_dist:
                # 값을 갱신해주고, 우선순위 큐에 해당 정보를 넣어줍니다.
                dist[target_index] = new_dist
                heapq.heappush(pq, (new_dist, target_index))


    return dist

dist = dijkstar(graph, k-1)
for i in dist:
    if i == float('inf'):
        print(-1)
    else:
        print(i)


# Please write your code here.
