from collections import deque

N, M = map(int, input().split())
mx, my, ex, ey = map(int, input().split())
info = list(map(int, input().split()))
man = [(info[i], info[i+1]) for i in range(0,len(info),2)]
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

def get_medusa_route():
    sx, sy = mx, my
    q = deque([(sx,sy, [])])
    visited = [[False]*N for i in range(N)]
    visited[sx][sy] = True
    while q:
        x, y, path = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1), (0,1)]:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 0:
                if (nx, ny) == (ex,ey):
                    return path
                q.append((nx, ny, path+[(nx,ny)]))
                visited[nx][ny] = True
    return -1

def view_up(x, y, man_arr):
    view = [[0]*N for i in range(N)]
    
    for i in range(x-1, -1, -1):
        left = max(0, y-(x-i))
        right = min(N-1, y+(x-i))
        for j in range(left, right+1):
            view[i][j] = 1

    found = False
    for i in range(x-1, -1, -1):
        if not found:
            view[i][y] = 1
        else:
            view[i][y] = 0
        
        if man_arr[i][y] > 0:
            found = True

    for h in range(x-1, -1, -1):
        #(x-1, x-2, ..., 0)
        left = max(0, y-(x-h))
        right = min(N-1, y+(x-h))
        for j in range(left, y):
        #(left, left +1, ... y-1)
            if view[h][j] == 0 or man_arr[h][j] > 0:
                if j > 0:
                    view[h-1][j-1] = 0 #왼쪽 위 시야 제거
                view[h-1][j] = 0 #바로 위 시야제거
        
        for j in range(y+1, right+1):
        #(y, y+1, ..., right+1)
            if view[h][j] == 0 or man_arr[h][j] > 0:
                if j+1 < N:
                    view[h-1][j+1] = 0 #왼쪽 위 시야 제거
                view[h-1][j] = 0 #바로 위 시야제거
    

    stone = 0
    for i in range(N):
        for j in range(N):
            if view[i][j] == 1 and man_arr[i][j] > 0:
                stone += man_arr[i][j]
    
    return stone, view
    

def view_down(x, y, man_arr):
    view = [[0]*N for i in range(N)]
    
    for i in range(x+1, N):
        left = max(0, y-(i-x))
        right = min(N-1, y+(i-x))
        for j in range(left, right+1):
            view[i][j] = 1

    found = False
    for i in range(x+1, N):
        if not found:
            view[i][y] = 1
        else:
            view[i][y] = 0
        
        if man_arr[i][y] > 0:
            found = True

    for i in range(x+1, N-1):
        left = max(0, y-(i-x))
        right = min(N-1, y+(i-x))
        for j in range(left, y):
            if view[i][j] == 0 or man_arr[i][j] > 0:
                if j > 0:
                    view[i+1][j-1] = 0 #왼쪽 아래 시야 제거
                view[i+1][j] = 0 #바로 아래 시야제거
        
        for j in range(y+1, right+1):
        #(y, y+1, ..., right+1)
            if view[i][j] == 0 or man_arr[i][j] > 0:
                if j+1 < N:
                    view[i+1][j+1] = 0 #왼쪽 아래 시야 제거
                view[i+1][j] = 0 #바로 아래 시야제거

    stone = 0
    for i in range(N):
        for j in range(N):
            if view[i][j] == 1 and man_arr[i][j] > 0:
                stone += man_arr[i][j]
    
    return stone, view
    

def view_left(x, y, man_arr):
    view = [[0]*N for i in range(N)]
    for i in range(y-1, -1, -1): #y-1부터 0 까지
        top = max(0, x - abs(y-i))
        bottom = min(N-1, x + abs(y-i))
        
        for j in range(top, bottom+1):
            view[j][i] = 1
    
    found = False
    for j in range(y-1, -1, -1):
        if found: 
            view[x][j] = 0
        else:
            view[x][j] = 1
        if man_arr[x][j] > 0:
            found = True

    for i in range(y-1, 0, -1): #y-1부터 0 까지
        top = max(0, x - abs(y-i))
        bottom = min(N-1, x + abs(y-i))
        #위쪽부터 건드려보자
        for j in range(top, x):
            if not view[j][i] or man_arr[j][i]:
                if j > 0:
                    view[j-1][i-1] = 0
                view[j][i-1] = 0
            
        for j in range(x+1, bottom+1):
            if not view[j][i] or man_arr[j][i]:
                if j+1 < N:
                    view[j+1][i-1] = 0
                view[j][i-1] = 0

    stone = 0
    for i in range(N):
        for j in range(N):
            if view[i][j] == 1 and man_arr[i][j] > 0:
                stone += man_arr[i][j]
    
    return stone, view



def view_right(x, y, man_arr):
    view = [[0]*N for i in range(N)]
    for i in range(y+1, N): 
        top = max(0, x - abs(y-i))
        bottom = min(N-1, x + abs(y-i))
        
        for j in range(top, bottom+1):
            view[j][i] = 1
    
    found = False
    for i in range(y+1, N): 
        if found: 
            view[x][i] = 0
        else:
            view[x][i] = 1
        if man_arr[x][i] > 0:
            found = True

    for i in range(y+1, N-1): 
        top = max(0, x - abs(y-i))
        bottom = min(N-1, x + abs(y-i))
        #위쪽부터 건드려보자
        for j in range(top, x):
            if not view[j][i] or man_arr[j][i]:
                if j > 0:
                    view[j-1][i+1] = 0
                view[j][i+1] = 0
            
        for j in range(x+1, bottom+1):
            if not view[j][i] or man_arr[j][i]:
                if j+1 < N:
                    view[j+1][i+1] = 0
                view[j][i+1] = 0

    stone = 0
    for i in range(N):
        for j in range(N):
            if view[i][j] == 1 and man_arr[i][j] > 0:
                stone += man_arr[i][j]
    return stone, view


def get_best_view(x, y, man_arr):
    #상하좌우
    best_direct = ''
    best_stone, best_view = -1, -1
    u_stone, u_v = view_up(x,y, man_arr)
    if u_stone > best_stone:
        best_stone = u_stone
        best_view = u_v
        best_direct = 'u'
    d_stone, d_v = view_down(x,y, man_arr)
    if d_stone > best_stone:
        best_stone = d_stone
        best_view = d_v
        best_direct = 'd'
    l_stone, l_v = view_left(x,y, man_arr)
    if l_stone > best_stone:
        best_stone = l_stone
        best_view = l_v
        best_direct = 'l'
    r_stone, r_v = view_right(x,y, man_arr)
    if r_stone > best_stone:
        best_stone = r_stone
        best_view = r_v
        best_direct = 'r'
    

    return best_stone, best_view



def move_man(cx, cy, view):
    move_cnt = 0
    killed = 0
    for i in range(len(man)):
        x,y = man[i]
        if (x,y) == (-1,-1): #사망자 처리
            continue
        if view[x][y] == 1: #돌이면 움직일 수 없음
            continue

        cur_dist = abs(cx - x) + abs(cy - y)
        for (dx, dy) in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx = x + dx
            ny = y + dy
            nex_dist = abs(cx - nx) + abs(cy - ny)
            if 0 <= nx < N and 0 <= ny < N and nex_dist < cur_dist and view[nx][ny] != 1:
                x = nx
                y = ny
                move_cnt += 1
                break
        
        cur_dist = abs(cx - x) + abs(cy - y)
        for (dx, dy) in [(0,-1), (0,1), (-1,0), (1,0)]:
            nx = x + dx
            ny = y + dy
            nex_dist = abs(cx - nx) + abs(cy - ny)
            if 0 <= nx < N and 0 <= ny < N and nex_dist < cur_dist and view[nx][ny] != 1:
                x = nx
                y = ny
                move_cnt += 1
                break
        
        #공격
        if (x,y) == (cx, cy):
            killed += 1
            man[i] = (-1,-1)
        else:
            man[i] = (x,y)

    return move_cnt, killed

route = get_medusa_route()
if route == -1:
    print(-1)
else:
    for (cx, cy) in route:
        for i in range(M):
            if man[i] == (cx,cy):
                man[i] = (-1,-1) #같은 자리에 있으면 사망

        man_arr = [[0]*N for i in range(N)]
        for i in range(len(man)):
            x, y = man[i]
            if (x,y) != (-1,-1):
                man_arr[x][y] += 1

        best_stone, best_view = get_best_view(cx, cy, man_arr)
        
        move_cnt, killed = move_man(cx, cy, best_view)
        
        print(move_cnt, best_stone, killed)
print(0)


