from queue import deque

N, M = map(int, input().split())
edges = []
for _ in range(M):
    s,e = map(int, input().split())
    edges.append([s,e])
    edges.append([e,s])

def bfs_solve(s, te, graph):
    queue = deque([s])
    history = []
    seen = set()
    
    while queue:
        current = queue.popleft()
        if current in seen:
            continue
        seen.add(current)
        history.append(current)
        if current == te:
            return history
        if current in graph:
            for neighbor in graph[current]:
                if neighbor not in seen:
                    queue.append(neighbor)
    return history


scores = []

for i in range(N):
    scores = []
    for j in range(N):    
        if i != j:
            print(bfs_solve(i+1,j+1,edges))
            scores.append(len(bfs_solve(i+1,j+1,edges))-1)
    print(i,scores)

print(scores)

graph = {}
for start, end in edges:
    if start not in graph:
        graph[start] = []
    graph[start].append(end)

all_scores = []
for i in range(1, N+1):
    scores = []
    for j in range(1, N+1):
        if i != j:
            path = bfs_solve(i, j, graph)
            scores.append(len(path) - 1)
    all_scores.append(scores)
    print(i, scores)
print(all_scores)