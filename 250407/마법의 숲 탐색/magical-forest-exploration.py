from collections import deque

R, C, K = map(int, input().split())
pawn = []
arr = [[0]*C for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(K):
    c, d = map(int, input().split())
    pawn.append((c-1, d))

def inbound(x, y):
    return 0 <= x < R and 0 <= y < C

def can_move(x, y):
    # 숲 내부이거나, 숲 위쪽에서 진입 중일 땐 True
    if 0 <= x < R and 0 <= y < C:
        return arr[x][y] == 0
    elif x < R and 0 <= y < C:
        return True
    return False

def init():
    for i in range(R):
        for j in range(C):
            arr[i][j] = 0

def move(pawn, idx):
    c, d = pawn
    x, y = -2, c  # 골렘 중심 시작 좌표

    while True:
        # 아래로 전진
        nx = x + 1
        ny = y
        if all(can_move(nx + dx[i], ny + dy[i]) for i in range(4)) and can_move(nx, ny):
            x, y = nx, ny
        # 왼쪽 회전
        elif all(can_move(x + dx[i] + 1, y + dy[i] - 1) for i in range(4)) and can_move(x + 1, y - 1):
            x += 1
            y -= 1
            d = (d - 1) % 4
        # 오른쪽 회전
        elif all(can_move(x + dx[i] + 1, y + dy[i] + 1) for i in range(4)) and can_move(x + 1, y + 1):
            x += 1
            y += 1
            d = (d + 1) % 4
        else:
            # 설치 시 몸통이 전부 숲 안에 있는지 확인
            if not inbound(x, y) or not all(inbound(x + dx[i], y + dy[i]) for i in range(4)):
                init()
                return (False, -1, -1)

            # 골렘 설치
            arr[x][y] = idx  # 중심
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if i == d:
                    arr[nx][ny] = -idx  # 출구
                    ex, ey = nx, ny     # 출구 위치 저장
                else:
                    arr[nx][ny] = idx
            return (True, ex, ey)

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited = [[False]*C for _ in range(R)]
    visited[sx][sy] = True
    max_row = sx

    while q:
        x, y = q.popleft()
        num = arr[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if inbound(nx, ny) and not visited[nx][ny]:
                # 같은 골렘 or 출구에서 다른 골렘 이동
                if abs(arr[nx][ny]) == abs(num):
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    max_row = max(max_row, nx)
                elif num < 0 and abs(arr[nx][ny]) != abs(num):
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    max_row = max(max_row, nx)
    return max_row

# 실행
answer = 0
for i in range(K):
    flag, sx, sy = move(pawn[i], i+1)
    if flag:
        score = bfs(sx, sy)
        answer += score + 1  # 0-based → 1-based
print(answer)
