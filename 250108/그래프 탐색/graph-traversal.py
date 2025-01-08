n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
visited = [False]*n
answer = 0
# Write your code here!

def dfs(visited, current_node):
    global answer
    for i in edges:
        if current_node in i:
            start, end = i
            if start == current_node:
                if not visited[end-1]:
                    visited[end-1] = True
                    dfs(visited, end)
                    answer += 1
            else:
                if not visited[start-1]:
                    visited[start-1] = True
                    dfs(visited, start)
                    answer += 1

visited[0] = True
dfs(visited, 1)
print(answer)