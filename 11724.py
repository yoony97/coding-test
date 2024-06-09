import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for e in graph[v]:
        if not visited[e]:
            dfs(e)

input = sys.stdin.read
data = input().split()
index = 0

N = int(data[index])
index += 1
M = int(data[index])
index += 1

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u = int(data[index])
    index += 1
    v = int(data[index])
    index += 1
    graph[u].append(v)
    graph[v].append(u)

component_count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        component_count += 1

print(component_count)
