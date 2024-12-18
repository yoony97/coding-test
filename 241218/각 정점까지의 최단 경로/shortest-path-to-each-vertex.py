import heapq
from collections import defaultdict

n, m = map(int, input().split())
k = int(input())

# 그래프 초기화 (인접 리스트)
graphs = defaultdict(list)
for i in range(m):
    s, e, w = map(int, input().split())
    graphs[s-1].append((e-1, w))  # 간선 정보 저장
    graphs[e-1].append((s-1, w))  # 무방향 그래프이므로 양방향 추가

def dijkstra(start):
    dist = [float('inf')] * n
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))  # (현재 거리, 현재 노드)
    
    while q:
        cd, current = heapq.heappop(q)
        if cd > dist[current]:
            continue
        
        # 현재 노드에서 모든 인접 노드 확인
        for neighbor, weight in graphs[current]:
            new_dist = cd + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(q, (new_dist, neighbor))
    
    return dist

# 시작 노드가 1번 노드라고 가정 (0-index 보정)
answer = dijkstra(k-1)
for i in answer:
    if i == float('inf'):
        print(-1)
    else:
        print(i)
