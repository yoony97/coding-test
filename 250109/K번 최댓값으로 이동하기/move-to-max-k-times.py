from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
q = deque([(r-1,c-1)])
dxs = [0, 0, -1, 1]
dys = [-1,1, 0, 0]

for _ in range(k):
    r, c =  q[0]
    threshold = grid[r][c]
    maximum = 0
    point  = (r,c)
    visitied = [[False]*n for _ in range(n)]
    visitied[r][c] = True
    while q:
        r, c = q.popleft()
        for i in range(4):
            nx = r + dxs[i]
            ny = c + dys[i]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] <  threshold and not visitied[nx][ny]:
                if maximum < grid[nx][ny]:
                    point = (nx, ny)
                    maximum  = grid[nx][ny]
    
                elif maximum == grid[nx][ny]:
                    if nx < point[0]:
                        point = (nx, ny)
                    elif nx == point[0]:
                        point = (nx, min(ny, point[1]))
                    maximum  = grid[nx][ny]
                
                visitied[nx][ny]= True
                q.append((nx,ny))
    q = deque([point])

print(point[0]+1, point[1]+1)
# Write your code here!
