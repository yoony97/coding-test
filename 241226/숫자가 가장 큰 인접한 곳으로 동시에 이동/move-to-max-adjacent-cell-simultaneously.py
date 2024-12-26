from collections import deque

n, m, t = map(int, input().split())
arr = []
start = []
for _ in range(n):
    arr.append(list(map(int,  input().split())))


for _ in range(m):
    x, y = map(int,  input().split())
    start.append((x-1, y-1))# 0-index

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = deque(start)

for _ in range(t):
    next_cont = [[0]*n for _ in range(n)]
    
    while start:
        x, y = start.popleft()
        max_value = -1 # arr[x][y]
        rx, ry = -1, -1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if max_value < arr[nx][ny]:
                    max_value = arr[nx][ny]
                    rx, ry = nx, ny
        
        if rx >= 0 and ry >= 0:
            next_cont[rx][ry] += 1
    
    start.clear()

    for i in range(n):
        for j in range(n):
            if next_cont[i][j] == 1:
                start.append((i,j))

        
print(len(start))