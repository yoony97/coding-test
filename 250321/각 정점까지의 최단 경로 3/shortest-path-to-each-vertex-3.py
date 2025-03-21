import heapq

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
visited = [[False]*n for i in range(n)]
graph = [[0]*n for i in range(n)]

for i in range(m):
    s, e, v = edges[i]
    graph[s-1][e-1] = v



def dijkstra(graph, source):
    visited = [False] * n
    dist = [float('inf')]*n    
    dist[source] = 0

    for i in range(n):
        min_index = -1
        for j in range(n):
            if visited[j]:
                continue
            
            if min_index == -1 or dist[min_index] > dist[j]:
                min_index = j
        
        visited[min_index] = True                
        for j in range(n):
            if graph[min_index][j] == 0:
                continue
            dist[j] = min(dist[j], dist[min_index]+ graph[min_index][j])
    
    return dist

start = 0
dist = dijkstra(graph, start)
for i in range(n):
    if i != start:
        print(dist[i])
