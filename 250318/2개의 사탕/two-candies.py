
from collections import deque

def init():
    global N, M, MAPS, exit
    N, M = map(int, input().split())
    MAPS = [[0]*M for _ in range(N)]
    red, blue, exit = None, None, None
    for row in range(N):
        inputs = input()
        for col in range(M):
            if inputs[col] == '#':
                MAPS[row][col] = -1
            else: 
                MAPS[row][col] = 0
            if inputs[col] == 'O':
                exit  = (row, col)# (y, x)
            if inputs[col] == 'R':
                red = (row, col)  # (y, x)
            if inputs[col] == 'B':
                blue = (row, col) # (y, x)
    return red, blue, exit
def move_ball(pos, dx, dy):
    y, x = pos
    count = 0
    while True:
        next_y = y + dy
        next_x = x + dx
        # 벽이면 이동 중지
        if MAPS[next_y][next_x] == -1:
            break
        # 구멍이면 그 위치로 이동 후 종료
        if (next_y, next_x) == exit:
            return (next_y, next_x), count + 1, True
        y, x = next_y, next_x
        count += 1
    return (y, x), count, False


def move(cr, cb, direct):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dy, dx = directions[direct]
    

    nr, r_count, r_hole = move_ball(cr, dx, dy)
    nb, b_count, b_hole = move_ball(cb, dx, dy)
           

    if r_hole and b_hole:
        return nr, nb, -1
    
    if b_hole:
        return nr, nb, -1

    if r_hole:
        return nr, nb, 1
    
    # 만약 두 공이 같은 위치에 있다면, 더 많이 이동한 공은 한 칸 뒤로 이동
    if nr == nb:
        if r_count > b_count:
            nr = (nr[0] - dy, nr[1] - dx)
        else:
            nb = (nb[0] - dy, nb[1] - dx)
    
    return nr, nb, 0

def solve():
    red, blue, exit = init()
    queue = deque([[red, blue, 0]])
    visited = [(red[0], red[1], blue[0], blue[1])] 
    while queue:
        cr, cb, cnt = queue.popleft()
        for i in range(4):
            nr, nb, flag = move(cr, cb, i)
            
            if flag == 1:
                return cnt+1
            
            elif flag == 0:
                if (nr[0], nr[1], nb[0], nb[1]) not in visited:
                    visited.append((nr[0], nr[1], nb[0], nb[1]))
                    queue.append([nr, nb, cnt+1])
    return -1

    
    
if __name__ == '__main__':
    answer= solve()
    if answer > 10:
        print(-1)
    else:
        print(answer)