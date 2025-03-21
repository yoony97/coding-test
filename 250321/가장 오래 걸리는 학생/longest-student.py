import heapq
n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[ ] for i in range(n)]

for i in range(m):
    s, e, v= edges[i]
    graph[s-1].append((e-1,v))
    graph[e-1].append((s-1,v))


def dijkstra(graph, source):
    pq = []
    dist = [float('inf')]*n
    dist[source] = 0
    heapq.heappush(pq, (0, source))
    while pq:
        min_dist, min_idx = heapq.heappop(pq)
        if min_dist != dist[min_idx]:
            continue
        
        for target_idx, target_dist in graph[min_idx]:
            new_dist = dist[min_idx] + target_dist
            if dist[target_idx] > new_dist:
                dist[target_idx] = new_dist
                heapq.heappush(pq, (new_dist, target_idx))
    return dist

print(max(dijkstra(graph, n-1)))

            



