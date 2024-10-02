import sys

data = sys.stdin.read().strip().split("\n")
N, M = map(int, data[0].split(" "))

table = [list(map(int, i.split(" "))) for i in data[1:N+1]]
target = [list(map(int, i.split(" "))) for i in data[N+1:]]

# 2차원 누적합 계산
sum_table = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum_table[i][j] = (
            table[i-1][j-1]
            + sum_table[i-1][j]
            + sum_table[i][j-1]
            - sum_table[i-1][j-1]
        )

# 쿼리 처리
for i in range(M):
    x1, y1, x2, y2 = target[i]
    # 인덱스 보정을 위해 -1
    result = (
        sum_table[x2][y2]
        - sum_table[x1-1][y2]
        - sum_table[x2][y1-1]
        + sum_table[x1-1][y1-1]
    )
    print(result)
