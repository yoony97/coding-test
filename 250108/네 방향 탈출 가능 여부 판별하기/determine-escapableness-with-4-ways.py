from collections import deque
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for i in range(n)]
queue = deque([(0,0)])
visited[0][0] = True
ispossible = False
dxs = [0, 0, -1, 1]
dys = [1, -1,  0,  0]
while queue:
    x, y = queue.popleft()
    if x == n-1 and y == m-1:
        ispossible = True
        break

    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] != 0 and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx,ny))

if ispossible:
    print(1)
else:
    print(0)
# Write your code here!
