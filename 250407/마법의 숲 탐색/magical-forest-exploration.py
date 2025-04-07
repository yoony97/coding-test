from collections import deque

R, C, K = map(int, input().split())
pawn = []
arr = [[0]*C for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(K):
    c, d = map(int, input().split())
    pawn.append((c-1,d))

def inbound(x, y):
    if 0 <= x < R and 0  <= y < C:
        return True
    return False


def can_move(x, y):
    if not inbound(x, y):  # 보드 밖이면
        if x < R and 0 <= y < C:  # 위쪽 바깥 영역은 허용
            return True
    else:  # 보드 안이면
        if arr[x][y] == 0:
            return True
    return False

def init():
    for i in range(R):
        for j in range(C):
            arr[i][j] = 0

def move(pawn, idx):
    c, d  = pawn
    x, y = -2, c #센터 좌표
    while True:
        nx = x+1
        ny = y
        #남쪽으로 직진 가능해?
        if can_move(nx+1, ny) and can_move(nx-1, ny) and can_move(nx, ny+1) and can_move(nx, ny-1) and can_move(nx,ny):
            x = nx
            y = ny
        #서쪽으로 회전 가능해?
        elif can_move(x, y-2) and can_move(x+1, y-1) and can_move(x-1, y-1) and can_move(x+2,y-1) and can_move(x+1, y-2):
            x = x+1
            y = y-1
            d = (d-1)%4
        #동쪽으로 회전 가능해?
        elif can_move(x, y+2) and can_move(x+1, y+1) and can_move(x-1, y+1) and can_move(x+2,y+1) and can_move(x+1, y+2):
            x = x+1
            y = y+1
            d = (d+1)%4
        elif not all(inbound(x + dx[i], y + dy[i]) for i in range(4)) or not inbound(x, y):
            init()
            return (False, -1, -1)
            

        else:
            arr[x][y] = idx
            ex = -1
            ey = -1
            for i in range(4):
                if i == d:
                    ex = x+dx[i]  
                    ey = y+dy[i]
                    arr[ex][ey] = -idx
                else:
                    arr[x+dx[i]][y+dy[i]] = idx
            return (True, ex, ey)
            
    
def bfs(x,y):
    q = deque([(x,y)])
    visited = [[False]*C for _ in range(R)]
    visited[x][y] = True
    max_row = x
    while q:
        cx, cy = q.popleft()
        num = arr[cx][cy]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if inbound(nx, ny) and not visited[nx][ny] and arr[cx][cy] != 0:
                if abs(arr[nx][ny]) == abs(num): # 같은 골램일 떼 이동
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    max_row = max(nx, max_row)
                elif num < 0 and abs(num) != abs(arr[nx][ny]): #출구 일때, 서로 다른 골렘에 이동 가능
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    max_row = max(nx, max_row)
    return max_row
            

#출구를 음수로 설정했어
#쌓이기 시작하면서 작은 값들이 밑으로 깔린다.
#따라서, 출구일 떄, 보다 

answer = 0
for i in range(K):
    flag, x, y= move(pawn[i],i+1)
    if flag:
        score = bfs(x,y)
        #print(score+1)
        answer += score+1

print(answer)