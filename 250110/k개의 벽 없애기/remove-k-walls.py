from collections import deque
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
answer = -1
r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1


def bfs():
    global answer
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque([(r1,c1)])
    cnt = [[0]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    visited[r1][c1] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 1:
                q.append((nx,ny))
                cnt[nx][ny] = cnt[x][y] + 1
                visited[nx][ny] = True

    if visited[r2][c2]:
        if answer == -1:
            answer = cnt[r2][c2]
        else:
            answer = min(answer, cnt[r2][c2])

def backtracking(cur):
    if cur == k:
        bfs()
        return

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                grid[i][j] = 0
                backtracking(cur+1)
                grid[i][j] = 1    
            
backtracking(0)
print(answer)

# Write your code here!
