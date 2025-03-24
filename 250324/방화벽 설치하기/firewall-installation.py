from collections import deque

n, m = map(int,input().split())
arr = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(n):
    arr.append(list(map(int,input().split())))

#일단 불이 상하좌우로 번져, 방화벽은 못 뚫음
#불은  2, 방화벽 1, 빈칸 0
def spread(new_arr):
    copyed = [[new_arr[j][i] for i in range(m)] for j in range(n)]
    result = 0
    q = deque([])
    for i in range(n):
        for j in range(m):
            if copyed[i][j] == 2:
                q.append((i,j))
    
    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < n and 0 <= ny < m and copyed[nx][ny] == 0:
                copyed[nx][ny] = 2
                q.append((nx,ny))
    
    for i in range(n):
        for j in range(m):
            if copyed[i][j] == 0:
                result += 1
    return result

answer = 0
def back(count, start):
    global answer
    if count == 3:
        answer = max(answer, spread(arr))
        return
    for idx in range(start, n * m):
        i = idx // m
        j = idx % m
        if arr[i][j] == 0:
            arr[i][j] = 1
            back(count + 1, idx + 1)
            arr[i][j] = 0

back(0, 0)
print(answer)
