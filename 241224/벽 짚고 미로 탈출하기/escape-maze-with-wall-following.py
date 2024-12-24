def escape_maze(N, start_x, start_y, grid):
    # 방향 정의 (우, 하, 좌, 상)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_dir = 0  # 처음에는 오른쪽을 바라봄
    x, y = start_x - 1, start_y - 1  # 0-index로 변환
    time = 0

    # 미로를 탈출할 때까지 반복
    while True:
        # 현재 방향으로 이동 가능한지 확인
        nx, ny = x + directions[current_dir][0], y + directions[current_dir][1]

        # 미로를 탈출한 경우
        if not (0 <= nx < N and 0 <= ny < N):
            return time + 1

        # 이동 가능한 경우
        if grid[nx][ny] == '.':
            # 오른쪽 벽 확인 (시계 방향의 다음 방향)
            right_dir = (current_dir + 1) % 4
            rx, ry = nx + directions[right_dir][0], ny + directions[right_dir][1]

            if 0 <= rx < N and 0 <= ry < N and grid[rx][ry] == '#':
                # 오른쪽에 벽이 있는 경우
                x, y = nx, ny
                time += 1
            else:
                # 오른쪽에 벽이 없는 경우
                x, y = nx, ny
                current_dir = right_dir
                time += 1
        else:
            # 이동 불가능한 경우 반시계 방향으로 회전
            current_dir = (current_dir - 1) % 4

        # 종료 조건: 현재 위치와 방향이 초기 상태로 돌아오면 -1 반환
        if (x, y, current_dir) == (start_x - 1, start_y - 1, 0):
            return -1



# 입력 처리
N = int(input())
start_x, start_y = map(int, input().split())
grid = [input().strip() for _ in range(N)]

# 결과 출력
result = escape_maze(N, start_x, start_y, grid)
print(result)
