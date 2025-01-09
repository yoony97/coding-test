from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]
r = [p[0] for p in points]
c = [p[1] for p in points]
dxs = [0,1, -1, 0]
dys = [1,0,0,-1]
cnt = 0
visited = [[False]*n for i in range(n)]
for i in range(k):
    x, y = r[i]-1, c[i]-1
    if not visited[x][y]:
        queue = deque([(x,y)])
        cnt+=1
        visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for j in range(4):
            nx = cx+dxs[j]
            ny = cy+dys[j]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))
                cnt += 1
print(cnt)
# Write your code here!
