n, m, t = map(int, input().split())
arr = []
start = []
for _ in range(n):
    arr.append(list(map(int,  input().split())))

for _ in range(m):
    start.append(tuple(map(int,  input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    next_cont = [[0]*n for _ in range(n)]
    
    while start:
        x, y = start.pop(0)
        max_value = 0 #arr[x][y]
        rx, ry = 0, 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if max_value < arr[nx][ny]:
                    max_value = arr[nx][ny]
                    rx, ry = nx, ny
        next_cont[rx][ry] += 1

    for i in range(n):
        for j in range(n):
            if next_cont[i][j] == 1:
                start.append((i,j))

        
print(len(start))