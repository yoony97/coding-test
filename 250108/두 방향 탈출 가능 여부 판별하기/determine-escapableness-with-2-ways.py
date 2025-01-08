n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1]
dy = [1, 0]
visited = [[False]*m for i in range(n)]

answer = 0
# Write your code here!

def dfs(x, y):
    global answer
    if x == n-1 and y == m-1:
        answer = 1
        return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx,ny)

visited[0][0] = True
dfs(0,0)
print(answer)