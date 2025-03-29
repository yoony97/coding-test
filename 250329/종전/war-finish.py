N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')

def ispossible(x, y, d1, d2):
    return (
        0 <= x < x + d1 + d2 < N and
        0 <= y - d1 < y < y + d2 < N
    )

for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if not ispossible(x, y, d1, d2):
                    continue
                
                board = [[0] * N for _ in range(N)]

                # 1. 경계선 그리기 (5로 표시)
                for i in range(d1 + 1):
                    board[x + i][y - i] = 5
                    board[x + d2 + i][y + d2 - i] = 5
                for i in range(d2 + 1):
                    board[x + i][y + i] = 5
                    board[x + d1 + i][y - d1 + i] = 5

                # 2. 경계선 내부 채우기
                for r in range(x + 1, x + d1 + d2):
                    start = -1
                    end = -1
                    for c in range(N):
                        if board[r][c] == 5:
                            if start == -1:
                                start = c
                            else:
                                end = c
                    if start != -1 and end != -1:
                        for c in range(start + 1, end):
                            board[r][c] = 5

                # 3. 각 부족 조건에 맞춰 나누기
                for r in range(N):
                    for c in range(N):
                        if board[r][c] != 0:
                            continue
                        # 1번 부족: (0 <= r < x + d1), (0 <= c <= y)
                        if 0 <= r < x + d1 and 0 <= c <= y:
                            board[r][c] = 1
                        # 2번 부족: (0 <= r <= x + d2), (y < c < N)
                        elif 0 <= r <= x + d2 and y < c < N:
                            board[r][c] = 2
                        # 3번 부족: (x + d1 <= r < N), (0 <= c < y - d1 + d2)
                        elif x + d1 <= r < N and 0 <= c < y - d1 + d2:
                            board[r][c] = 3
                        # 4번 부족: (x + d2 < r < N), (y - d1 + d2 <= c < N)
                        elif x + d2 < r < N and y - d1 + d2 <= c < N:
                            board[r][c] = 4
                        else:
                            board[r][c] = 5  # 경계나 내부는 이미 5번으로 처리됨

                # 4. 인구수 계산
                count = [0] * 5
                for r in range(N):
                    for c in range(N):
                        count[board[r][c] - 1] += arr[r][c]

                answer = min(answer, max(count) - min(count))

print(answer)
