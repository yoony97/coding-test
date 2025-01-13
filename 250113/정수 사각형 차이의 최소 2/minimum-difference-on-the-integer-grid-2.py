import sys

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def dfs(x, y, max_val, min_val, grid, memo):
    n = len(grid)

    # 도착 지점에 도달했을 때 최댓값과 최솟값 차이를 반환
    if x == n - 1 and y == n - 1:
        return max_val - min_val

    # 메모이제이션 (현재 좌표에서 max_val, min_val 상태를 기록)
    if (x, y, max_val, min_val) in memo:
        return memo[(x, y, max_val, min_val)]

    # 이동 가능한 방향: 오른쪽, 아래쪽
    directions = [(0, 1), (1, 0)]
    min_diff = sys.maxsize

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            new_max = max(max_val, grid[nx][ny])
            new_min = min(min_val, grid[nx][ny])
            min_diff = min(min_diff, dfs(nx, ny, new_max, new_min, grid, memo))

    memo[(x, y, max_val, min_val)] = min_diff
    return min_diff

def min_difference_path(grid):
    n = len(grid)
    memo = {}
    return dfs(0, 0, grid[0][0], grid[0][0], grid, memo)

# 실행
print(min_difference_path(grid))  # 최소 차이 출력
