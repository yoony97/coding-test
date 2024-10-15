import sys

data = sys.stdin.read().strip().split("\n")
N = int(data[0])
maps = []
for i in data[1:]:
    maps.append(list(map(int, i.split())))
S = [[0] * (N + 1) for _ in range(N + 1)]
# 누적합 행렬 계산
for i in range(1, N + 1):
    for j in range(1, N + 1):
        # maps[i-1][j-1]을 사용해 원본 행렬의 값 접근
        S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + maps[i - 1][j - 1]

# 구간 합 계산 함수
def get_sum(x1, y1, x2, y2):
    # (x1, y1)부터 (x2, y2)까지의 구간 합 계산
    return S[x2 + 1][y2 + 1] - S[x1][y2 + 1] - S[x2 + 1][y1] + S[x1][y1]
ans = -1*float('inf')

print(S)

for start_x in range(N):
    for start_y in range(N):
        for end_x in range(start_x, N):  # start_x <= end_x
            for end_y in range(start_y, N):
                #print(start_x, start_y, end_x, end_y, get_sum(start_x, start_y, end_x, end_y))
                ans = max(ans, get_sum(start_x, start_y, end_x, end_y))

print(ans)