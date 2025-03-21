n, m = map(int, input().split())
k = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[0]*n for _ in range(n)]

for i in range(m):
    s, e, v = edges[i]
    graph[s-1][e-1] = v
    graph[e-1][s-1] = v

def dijkstar(graph, source):
    dist = [float('inf')]*n
    visited = [False]*n
    dist[source] = 0
    
    for _ in range(n):
        
        min_idx = -1
        for j in range(n):
            if visited[j]:
                continue
            
            if min_idx == -1 or dist[min_idx] > dist[j]:
                min_idx = j
        
        visited[min_idx] = True

        #거리 업데이트
        for j in range(n):
            if graph[min_idx][j] != 0: #인접하다면
                dist[j] = min(dist[j], dist[min_idx] + graph[min_idx][j])
        

    return dist

dist = dijkstar(graph, k-1)
for i in dist:
    if i == float('inf'):
        print(-1)
    else:
        print(i)


# Please write your code here.
