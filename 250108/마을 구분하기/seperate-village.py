n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for i in range(n)]
number = 0
answer = []
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]
# Write your code here!
def dfs(x,y):
    global number
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            number += 1
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            visited[i][j] = True
            number = 1
            dfs(i,j)
            answer.append(number)

print(len(answer))
answer.sort()
for i in answer:
    print(i)