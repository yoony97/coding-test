import sys
import collections

def bfs(start, graph):
    queue = collections.deque([start])
    distances = [-1] * len(graph)
    distances[start] = 0
    farthest_node = start
    max_distance = 0
    
    while queue:
        node = queue.popleft()
        for neighbor, weight in graph[node]:
            if distances[neighbor] == -1:
                queue.append(neighbor)
                distances[neighbor] = distances[node] + weight
                if distances[neighbor] > max_distance:
                    max_distance = distances[neighbor]
                    farthest_node = neighbor
    
    return farthest_node, max_distance

input_data = sys.stdin.read().strip().split("\n")
N = int(input_data[0])
graph = [[] for _ in range(N)]

for line in input_data[1:]:
    data = list(map(int, line.split()))
    u = data[0] - 1
    for i in range(1, len(data) - 1, 2):
        v = data[i] - 1
        cost = data[i+1]
        graph[u].append((v, cost))
        graph[v].append((u, cost))  # 양방향 그래프

# 임의의 노드에서 가장 먼 노드 찾기
farthest_node, max_distance = bfs(0, graph)
# 그 노드에서 가장 먼 노드와의 거리가 트리의 지름
_, diameter = bfs(farthest_node, graph)
print(diameter)
