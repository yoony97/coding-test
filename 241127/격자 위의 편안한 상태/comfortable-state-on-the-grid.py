#. ‘편안한 상태’란 방금 막 칠해진 칸을 기점으로 위 아래 양옆으로 인접한 4개의 칸 중 격자를 벗어나지 않는 칸에 색칠되어 있는 칸이 정확히 3개인 경우를 뜻합니다. 

N, M = map(int, input().split())
maps = [[0]*N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(M):
    col, row = map(int, input().split())
    col= col-1
    row = row - 1
    
    maps[col][row] = 1
    
    cnt = 0
    
    for k in range(4):
        nc = col + dy[k]
        nr = row + dx[k]

        if 0 <= nc < N and 0 <= nr < N and maps[nc][nr] == 1:
            cnt += 1
    if cnt == 3:
        print(1)
    else:
        print(0)