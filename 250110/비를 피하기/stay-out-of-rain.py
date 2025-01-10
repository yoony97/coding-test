from collections import deque
n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer  = [[-1]*n  for i in range(n)]
count = [[0]*n  for i in range(n)]
visited =  [[False]*n  for i in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(i,j):
    visited =  [[False]*n  for i in range(n)]
    q = deque([(i,j,0)])
    visited[i][j] = True
    while q:
        
        x, y, dist = q.popleft()
        if  grid[x][y] == 2:
            if answer[x][y] == -1:
                answer[x][y] = dist
                count[i][j]+= 1
            else:
                if answer[x][y] > dist:
                    answer[x][y] = dist
                    count[i][j] += 1
        
        if count[i][j] >= h:
            return

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and not grid[nx][ny] ==1:
                q.append((nx,ny, dist+1))
                visited[nx][ny] = True
            
for i in range(n):
    for j in range(n):
        if grid[i][j] == 3:
            bfs(i,j)            
            answer[i][j] = 0
        elif grid[i][j] == 1 or grid[i][j] == 0:
            answer[i][j] = 0

for i in range(n):
    for j in range(n):
        print(answer[i][j], end =' ')
    print()