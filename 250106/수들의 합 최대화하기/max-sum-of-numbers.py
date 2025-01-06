
import sys

n = int(sys.stdin.readline().strip())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = 0
max_vals = [max(row) for row in grid]  # 각 행의 최댓값 (가지치기 용도)

def solve(cnt, curr_sum, col_mask):
    global answer
    if curr_sum + sum(max_vals[cnt:]) <= answer:  # 앞으로 가능한 최댓값보다 answer가 크면 중단
        return
    
    if cnt == n:
        answer = max(answer, curr_sum)
        return

    for j in range(n):
        if not (col_mask & (1 << j)):  # 비트마스크를 이용하여 열 중복 체크
            solve(cnt + 1, curr_sum + grid[cnt][j], col_mask | (1 << j))  # 해당 열 사용 처리

solve(0, 0, 0)
print(answer)