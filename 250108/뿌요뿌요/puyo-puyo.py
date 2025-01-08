n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for i in range(n)]
boom = 0
answer = []
blocks = []
# Write your code here!
def dfs(x,y,current):
    global boom 
    dxs = [0, 0, -1, 1]
    dys = [1, -1, 0, 0]
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == current:
            visited[nx][ny] = True
            boom += 1
            dfs(nx, ny, current)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            boom = 1
            visited[i][j] = True
            dfs(i, j, grid[i][j])
            blocks.append(boom)
            if boom >= 4:            
                answer.append(boom)

if answer:
    print(len(answer), max(blocks))
else:
    print(0, max(blocks))