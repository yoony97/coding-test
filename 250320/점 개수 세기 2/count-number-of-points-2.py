from sortedcontainers import SortedSet
import sys

input = sys.stdin.read
data = input().splitlines()

n, q = map(int, data[0].split())
points = [tuple(map(int, line.split())) for line in data[1:n+1]]
queries = [tuple(map(int, line.split())) for line in data[n+1:]]

# Step 1: 좌표 압축을 위한 x, y 값 수집
xs = SortedSet(x for x, y in points)
ys = SortedSet(y for x, y in points)

# 압축된 좌표 매핑
x_map = {v: i for i, v in enumerate(xs)}
y_map = {v: i for i, v in enumerate(ys)}

# 압축된 좌표 크기
X = len(xs)
Y = len(ys)

# Step 2: Grid (2D 배열) 생성 및 점 개수 저장
grid = [[0] * (Y + 1) for _ in range(X + 1)]

# 압축된 좌표에 점 저장
for x, y in points:
    grid[x_map[x]][y_map[y]] += 1

# Step 3: 2D 누적합 (Prefix Sum) 계산
prefix = [[0] * (Y + 1) for _ in range(X + 1)]

for i in range(X):
    for j in range(Y):
        prefix[i+1][j+1] = (
            prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + grid[i][j]
        )

# Step 4: 쿼리 처리 (O(1) 조회)
results = []
for x1, y1, x2, y2 in queries:
    if x1 > xs[-1] or x2 < xs[0] or y1 > ys[-1] or y2 < ys[0]:  # 범위 벗어난 경우
        results.append("0")
        continue

    # 압축된 인덱스 범위 가져오기
    x1_idx = x_map[x1] if x1 in x_map else xs.bisect_left(x1)
    x2_idx = x_map[x2] if x2 in x_map else xs.bisect_right(x2) - 1
    y1_idx = y_map[y1] if y1 in y_map else ys.bisect_left(y1)
    y2_idx = y_map[y2] if y2 in y_map else ys.bisect_right(y2) - 1

    # 2D Prefix Sum으로 O(1) 연산
    result = (
        prefix[x2_idx+1][y2_idx+1]
        - prefix[x1_idx][y2_idx+1]
        - prefix[x2_idx+1][y1_idx]
        + prefix[x1_idx][y1_idx]
    )
    
    results.append(str(result))

# 출력
sys.stdout.write("\n".join(results) + "\n")
