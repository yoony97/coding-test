
n, m = map(int, input().split())
graphs = [[0]*n for _ in range(n)]
for i in range(m):
    s, e, w = map(int, input().split())
    graphs[s-1][e-1] = w

def dijkstra(s):
    dist = [float('inf')]*n
    dist[s-1] = 0
    q = [s-1]
    while q:
        current = q.pop(0)
        for i in range(n):
            if dist[i] > dist[current] + graphs[current][i] and graphs[current][i] != 0:
                dist[i] =  dist[current] + graphs[current][i]
                q.append(i)
    return dist

answer = dijkstra(1)
for i in answer:
    if i != 0:
        if i != float('inf'): 
            print(i)
        else:
            print(-1)