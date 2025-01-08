n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_height = max(max([grid[i] for i in range(n)]))
# Write your code here!
dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]
def dfs(x, y, k, visited):
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > k and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, k, visited)

answer = 0
answer_k = 0
for k in range(1,max_height+1):
    safty = 0
    visited = [[False]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > k:
                dfs(i,j, k, visited)
                safty += 1
    if answer < safty:
        answer = safty
        answer_k = k

print(answer_k, answer)

