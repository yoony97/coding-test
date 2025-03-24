N, M = map(int, input().split())
x, y, d = map(int, input().split())
arr = []
visited = [[0]*M for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    arr.append(line)

visited[x][y] =  1

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1] #북동남서
cnt = 0

def simulation(x, y, d):
    cnt = 0
    while cnt < 4:
        d = (d - 1 +4)%4  # 좌회전
        lx = x + dx[d] 
        ly = y + dy[d]
        if 0 <= lx < N and 0 <= ly < M: #격자 안?
            if arr[lx][ly] == 0 and visited[lx][ly] == 0: # 전진 가능해/
                visited[lx][ly] = 1
                return lx, ly, d
        cnt += 1

    bx = x - dx[d]
    by = y - dy[d]
    if 0 <= bx < N and 0 <= by < M:
        if arr[bx][by] == 0:
            return bx, by, d
        else:
            return -1, -1, -1



while True:
    x, y, d = simulation(x, y, d)
    if x == -1 and y == -1 and d == -1:
        break



answer = 0
for i in range(N):
    answer += sum(visited[i])
print(answer)