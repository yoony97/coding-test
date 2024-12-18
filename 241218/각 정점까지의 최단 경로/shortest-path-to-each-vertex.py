import heapq

n, m = map(int, input().split())
k = int(input())
graphs = [[float('inf')]*n for _ in range(n)]

# 그래프 초기화
for i in range(m):
    s, e, w = map(int, input().split())
    graphs[s-1][e-1] = w  # 노드 번호가 1부터 시작하므로 -1 보정
    graphs[e-1][s-1] = w

def dijkstra(start):
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n  # 방문 여부 확인용
    q = []
    heapq.heappush(q, (0, start))  # (현재 거리, 현재 노드)
    
    while q:
        cd, current = heapq.heappop(q)
        if visited[current]:
            continue
        visited[current] = True
    
        # 현재 노드에서 모든 다른 노드로의 거리 갱신
        for i in range(n):
            if graphs[current][i] != float('inf'):  # 간선이 있는 경우
                new_dist = cd + graphs[current][i]
                if new_dist < dist[i]:
                    dist[i] = new_dist
                    heapq.heappush(q, (new_dist, i))
    
    return dist

# 시작 노드가 1번 노드라고 가정 (0-index 보정)
answer = dijkstra(k-1)
for i in answer:
    if i == float('inf'):
        print(-1)
    else:
        print(i)
