import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def min_difference_path(grid):
    n = len(grid)

    # DP 테이블 초기화
    dp = [[sys.maxsize] * n for _ in range(n)]
    max_value = [[0] * n for _ in range(n)]
    min_value = [[0] * n for _ in range(n)]

    # 시작점 초기화
    dp[0][0] = 0
    max_value[0][0] = grid[0][0]
    min_value[0][0] = grid[0][0]


    for j in range(1, n):
        max_value[0][j] = max(max_value[0][j-1], grid[0][j])
        min_value[0][j] = min(min_value[0][j-1], grid[0][j])
        dp[0][j] = max_value[0][j] - min_value[0][j]


    for i in range(1, n):
        max_value[i][0] = max(max_value[i-1][0], grid[i][0])
        min_value[i][0] = min(min_value[i-1][0], grid[i][0])
        dp[i][0] = max_value[i][0] - min_value[i][0]

    # DP 테이블 채우기
    for i in range(1, n):
        for j in range(1, n):
            # 왼쪽에서 오는 경우
            left_max = max(max_value[i][j-1], grid[i][j])
            left_min = min(min_value[i][j-1], grid[i][j])
            left_diff = left_max - left_min

            # 위쪽에서 오는 경우
            up_max = max(max_value[i-1][j], grid[i][j])
            up_min = min(min_value[i-1][j], grid[i][j])
            up_diff = up_max - up_min

            # 최적 경로 선택
            if left_diff < up_diff:
                max_value[i][j] = left_max
                min_value[i][j] = left_min
                dp[i][j] = left_diff
            else:
                max_value[i][j] = up_max
                min_value[i][j] = up_min
                dp[i][j] = up_diff

    return dp[n-1][n-1]


print(min_difference_path(grid))
