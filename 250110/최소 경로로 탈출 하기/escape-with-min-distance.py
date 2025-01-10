from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
q = deque([(0,0,0)])
visited = [[False]*m for i in range(n)]
visited[0][0] = True
dxs = [1,-1,0,0]
dys = [0,0,-1,1]

while q:
    x, y, dist = q.popleft()
    if x == n-1 and y == m-1:
        print(dist)
        break
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx,ny,dist+1))


# Write your code here!
