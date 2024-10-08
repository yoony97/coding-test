import sys

# 입력 받기
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 테트로미노의 모든 형태 정의
tetrominoes = [
    # 길이 4짜리 막대 모양
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    # 정사각형 모양
    [(0,0), (0,1), (1,0), (1,1)],
    # L자 모양
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,2), (1,0), (1,1), (1,2)],
    # 번개 모양
    [(0,0), (1,0), (1,1), (2,1)],
    [(0,1), (1,0), (1,1), (2,0)],
    [(0,0), (0,1), (1,1), (1,2)],
    [(1,0), (1,1), (0,1), (0,2)],
    # T자 모양
    [(0,0), (0,1), (0,2), (1,1)],
    [(1,0), (1,1), (1,2), (0,1)],
    [(0,0), (1,0), (2,0), (1,1)],
    [(1,0), (0,1), (1,1), (2,1)],
    # L자 대칭 모양
    [(0,1), (1,1), (2,1), (2,0)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (1,0), (2,0), (0,1)],
]

max_sum = 0  # 최대 합계를 저장할 변수

# 격자 탐색
for i in range(N):
    for j in range(M):
        for tetro in tetrominoes:
            current_sum = 0
            is_valid = True
            for dx, dy in tetro:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < N and 0 <= ny < M:
                    current_sum += grid[nx][ny]
                else:
                    is_valid = False
                    break
            if is_valid:
                max_sum = max(max_sum, current_sum)

print(max_sum)
