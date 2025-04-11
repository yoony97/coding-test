
"""
시간의 벽 단면도 ( 윗면과 동서남북 네면 )
"""
from collections import deque

flue_dx = [0, 0, 1, -1]
flue_dy = [1, -1, 0, 0]
left_nxt = {0:2, 2:1, 1:3, 3:0}
right_nxt = {0:3, 2:0, 1:2, 3:1}
EAST, WEST, NORTH, SOUTH, TOP = 0, 1, 2, 3, 4
N, M, F = map(int, input().split())
arr = []
cube = []
isfirst_3d = False
left_top = []
right_bottom = []
exit = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 4:
            exit = [i,j]
        if row[j] == 3 and not isfirst_3d:
            isfirst_3d = True
            left_top = [i,j]
            right_bottom = [i + M - 1, j + M - 1]
    arr.append(row)


start = []
found_start = False
for i in range(5):
    temp = []
    if i == TOP:
        found_start = True
    for r in range(M):
        row = list(map(int, input().split()))
        if found_start:
            for c in range(M):
                if row[c] == 2:
                    start = [r, c]
        temp.append(row)
    cube.append(temp)

flue = []
for i in range(F):
    r, c, d, v = map(int, input().split())
    flue.append((r,c,d,v))

def find_exit(arr, left_top, right_bottom):
    lx, ly = left_top
    rx, ry = right_bottom
    d3_exit = [-1, -1]
    for i in range(lx, rx+1):
        for j in range(ly, ry+1):
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if arr[nx][ny] == 0:
                        d3_exit = [nx, ny]
                        break


    if d3_exit == [-1, -1]:
        return [-1,-1] #못찾음
    #찾고 동서남북 중 어디니 찾아야함
    else:
        x, y = d3_exit
        temp = []
        direct = -1
        if lx <= x <= rx and y > ry:  # 동쪽이 출구다.
            direct = EAST
            rl_x = abs(x - M - 1)
            temp = [M - 1, rl_x]
            # print(d3_exit)

        if lx <= x <= rx and y < ly:  # 서쪽이 출구다.
            direct = WEST
            rlx = abs(x - M - 1)
            temp = [M - 1, M - 1 - rlx]


        if x > rx and ly <= y <= ry: #남쪽이 출구다
            direct = SOUTH
            rly = abs(M - 1 - y)
            temp = [M - 1, rly]

        if x < lx and ly <= y <= ry: #북쪽이 출구다
            direct = NORTH
            rly = abs(y - M-1)
            temp = [M-1 , rly]


        return direct, temp, d3_exit


def bfs_3d(sk, si, sj,ek, ei, ej):
    q = deque()
    v = [[[0]*M for _ in range(M)] for _ in range(5)]

    q.append((sk,si,sj))
    v[sk][si][sj]=1

    while q:
        ck,ci,cj = q.popleft()

        if (ck,ci,cj)==(ek,ei,ej):
            # myprint_3d(v)
            return v[ck][ci][cj]

        # 네방향, 범위내/범위밖->다른평명 이동처리, 미방문
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj

            # 범위밖
            if ni<0:    # 위쪽 범위 이탈
                if ck==0:   nk,ni,nj = 4,(M-1)-cj,M-1
                elif ck==1: nk,ni,nj = 4,cj,0
                elif ck==2: nk,ni,nj = 4,M-1,cj
                elif ck==3: nk,ni,nj = 4,0,(M-1)-cj
                elif ck==4: nk,ni,nj = 3,0,(M-1)-cj
            elif ni>=M: # 아래쪽 범위이탈
                if ck==4:   nk,ni,nj = 2,0,cj
                else:       continue
            elif nj<0:  # 왼쪽 범위이탈
                if ck==4:   nk,ni,nj = 1,0,ci
                else:
                    nk,ni,nj = left_nxt[ck],ci,M-1
            elif nj>=M: # 오른쪽 범위이탈
                if ck==4:   nk,ni,nj = 0,0,(M-1)-ci
                else:
                    nk,ni,nj = right_nxt[ck],ci,0
            else:       # 이탈아니면 같은 평면
                nk=ck

            # 미방문, 조건 맞으면
            if v[nk][ni][nj]==0 and cube[nk][ni][nj]==0:
                q.append((nk,ni,nj))
                v[nk][ni][nj]=v[ck][ci][cj]+1

    # 이곳에 왔다는건? 경로 없음!
    # myprint_3d(v)
    return -1

di=[ 0, 0, 1,-1]
dj=[ 1,-1, 0, 0]
def spread(flue, ei, ej):
    v = [[401] * N for _ in range(N)]
    for wi, wj, wd, wv in flue:  # wv 단위로 wd방향으로 확산표시(출구가 아닌경우만 확산)
        v[wi][wj] = 1
        for mul in range(1, N + 1):
            wi, wj = wi + di[wd], wj + dj[wd]
            if 0 <= wi < N and 0 <= wj < N and arr[wi][wj] == 0 and (wi, wj) != (ei, ej):
                if v[wi][wj] > wv * mul:  # 더 큰 값 일때만 갱신(겹칠수있으니)
                    v[wi][wj] = wv * mul
            else:
                break

    return v


def bfs_2d(sx_2d, sy_2d, flue_arr, arr, cnt):
    q = deque([(sx_2d,sy_2d, cnt)])
    visited = [[False]*N for _ in range(N)]
    visited[sx_2d][sy_2d] = True
    while q:
        #print(q)
        x, y, t = q.popleft()
        if x == exit[0] and y == exit[1]:
            return t
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if arr[nx][ny] == 0 and t+1 < flue_arr[nx][ny] :
                    q.append((nx,ny, t+1))
                    visited[nx][ny] = True
                elif arr[nx][ny] == 4:
                    return t+1

    return -1


flue_arr = spread(flue, exit[0], exit[1])
direct, temp, d3_exit = find_exit(arr, left_top, right_bottom)
time = bfs_3d(TOP, start[0], start[1], direct, temp[0], temp[1])
answer = bfs_2d(d3_exit[0], d3_exit[1], flue_arr, arr, time)
print(answer)

