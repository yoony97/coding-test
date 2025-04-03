from copy import deepcopy

# 8방향: 위부터 반시계 방향
# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

theifs = []
exist = [[0]*4 for _ in range(4)]

for row in range(4):
    info = list(map(int, input().split()))
    col = 0
    for i in range(0, len(info), 2):
        theifs.append((info[i], info[i+1]-1, row, col))  # (번호, 방향, x, y)
        exist[row][col] = info[i]
        col += 1

# 술래가 (0,0) 위치에 있는 도둑을 잡고 시작
theifs.sort(key=lambda x: x[0])
for i, t in enumerate(theifs):
    if t[2] == 0 and t[3] == 0:
        score = t[0]
        cap = (0, 0, t[1])
        exist[0][0] = 0
        theifs = theifs[:i] + theifs[i+1:]
        break

answer = 0

def change_direct(theif, exist, cap_pos, idx):
    p, d, x, y = theif[idx]
    for _ in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (cap_pos[0], cap_pos[1]):
            if exist[nx][ny] != 0:
                for i in range(len(theif)):
                    if theif[i][0] == exist[nx][ny]:
                        theif[i], theif[idx] = (theif[i][0], theif[i][1], x, y), (p, d, nx, ny)
                        exist[x][y], exist[nx][ny] = theif[i][0], theif[idx][0]
                        return
            else:
                theif[idx] = (p, d, nx, ny)
                exist[nx][ny], exist[x][y] = p, 0
                return
        d = (d + 1) % 8
    theif[idx] = (p, d, x, y)

def theif_turn(theif, exist, cap_pos):
    theif.sort(key=lambda x: x[0])
    for idx in range(len(theif)):
        p, d, x, y = theif[idx]
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (cap_pos[0], cap_pos[1]):
            if exist[nx][ny] != 0:
                for i in range(len(theif)):
                    if theif[i][0] == exist[nx][ny]:
                        theif[i], theif[idx] = (theif[i][0], theif[i][1], x, y), (p, d, nx, ny)
                        exist[x][y], exist[nx][ny] = theif[i][0], theif[idx][0]
                        break
            else:
                theif[idx] = (p, d, nx, ny)
                exist[nx][ny], exist[x][y] = p, 0
        else:
            change_direct(theif, exist, cap_pos, idx)
    return theif, exist

def attack_turn(cap_pos, target, exist, theif):
    tx, ty = target
    target_num = exist[tx][ty]
    for i in range(len(theif)):
        if theif[i][0] == target_num:
            new_dir = theif[i][1]
            theif = theif[:i] + theif[i+1:]
            break
    exist[tx][ty] = 0
    return (tx, ty, new_dir), theif, exist, target_num

def can_go(x, y, exist):
    return 0 <= x < 4 and 0 <= y < 4 and exist[x][y] != 0

def btk(current_state, theif, exist, score):
    global answer
    x, y, d = current_state

    # 도둑들 이동
    theif = deepcopy(theif)
    exist = deepcopy(exist)
    theif, exist = theif_turn(theif, exist, (x, y))

    moved = False
    for step in range(1, 4):
        nx, ny = x + dx[d]*step, y + dy[d]*step
        if can_go(nx, ny, exist):
            moved = True
            new_state, new_theif, new_exist, val = attack_turn((x, y), (nx, ny), deepcopy(exist), deepcopy(theif))
            btk(new_state, new_theif, new_exist, score + val)

    if not moved:
        answer = max(answer, score)

btk(cap, theifs, exist, score)
print(answer)