from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
dxs = [-2, -1, -2, -1, 2, 1, 2, 1]
dys = [-1, -2, 1, 2, -1, -2, 1, 2]
# Write your code here!
q = deque([(r1-1, c1-1, 0)])
visited = [[False]*n for _ in range(n)]
visited[r1-1][c1-1] = True
answer = -1
while q:
    x, y, dist = q.popleft()
    if x+1 == r2 and y+1 == c2:
        answer = dist
        break
    for i in range(8):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            q.append((nx,ny,dist+1))
            visited[nx][ny] = True

print(answer)