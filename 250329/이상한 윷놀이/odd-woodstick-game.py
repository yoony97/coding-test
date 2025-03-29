n, k = map(int, input().split())

# 색상 정보: 0=흰, 1=빨, 2=파
board_color = [list(map(int, input().split())) for _ in range(n)]

# 말 정보: [(x, y, direction)], 0-indexed
pieces = []
board = [[[] for _ in range(n)] for _ in range(n)]

# 방향: 우, 좌, 상, 하
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 방향 반전 맵
reverse_dir = {0: 1, 1: 0, 2: 3, 3: 2}

for i in range(k):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    d -= 1
    pieces.append([x, y, d])
    board[x][y].append(i)  # 말 번호만 저장

def move():
    for idx in range(k):
        x, y, d = pieces[idx]
        # 현재 말이 보드 위에서 어느 위치에 있는지 확인
        stack = board[x][y]
        height = stack.index(idx)
        move_stack = stack[height:]
        board[x][y] = stack[:height]

        nx = x + dx[d]
        ny = y + dy[d]

        # 보드 밖이거나 파란 칸
        if not (0 <= nx < n and 0 <= ny < n) or board_color[nx][ny] == 2:
            d = reverse_dir[d]
            pieces[idx][2] = d  # 방향 반전 저장
            nx = x + dx[d]
            ny = y + dy[d]
            # 반대 방향도 파란색 or 범위 밖이면 원래 자리로 되돌림
            if not (0 <= nx < n and 0 <= ny < n) or board_color[nx][ny] == 2:
                board[x][y].extend(move_stack)
                continue

        # 흰색
        if board_color[nx][ny] == 0:
            board[nx][ny].extend(move_stack)
        # 빨간색
        elif board_color[nx][ny] == 1:
            board[nx][ny].extend(reversed(move_stack))

        # 이동한 말들의 위치 갱신
        for piece_num in move_stack:
            pieces[piece_num][0], pieces[piece_num][1] = nx, ny

        # 종료 조건
        if len(board[nx][ny]) >= 4:
            return True
    return False

turn = 1
while turn <= 1000:
    if move():
        print(turn)
        break
    turn += 1
else:
    print(-1)
