from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())    
    start = deque([])
    
    for _ in range(M):
        x, y, d = input().split()
        if d == 'U':
            d = 0
        if d == 'D':
            d = 1
        if d == 'R':
            d = 3 
        if d == 'L':
            d = 2
        start.append((int(x)-1,int(y)-1,d))

    for _ in range(2*N):
        arr = [[0]*N for _ in range(N)]
        direct = [[0]*N for _ in range(N)]
        while start:
            x, y, d = start.popleft()
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                arr[nx][ny] += 1
                direct[nx][ny] = d
            else:
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                else:
                    d = 2
                direct[x][y] = d
                arr[x][y] += 1
        
        start.clear()
        for i in range(N):
            for j in range(N):
                #print(arr[i][j], end = ' ')
                if arr[i][j] == 1:
                    start.append((i, j, direct[i][j]))
            #print()
        #print()
    print(len(start))

