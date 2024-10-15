N, K = map(int,input().split())
maps = [[0]*(N+1) for _ in range(N+1)]
S = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    li = list(map(int,input().split()))
    for j in range(N):
        maps[i+1][j+1] = li[j]

for i in range(1, N+1):
    for j in range(1, N+1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + maps[i][j]
# 4. 구간 합 함수 (경계 체크 포함)
def get_sum(S, x1, y1, x2, y2):
    # 구간의 경계를 안전하게 클리핑
    x1 = max(1, min(x1, N))
    y1 = max(1, min(y1, N))
    x2 = max(1, min(x2, N))
    y2 = max(1, min(y2, N))

    # 구간 합 계산
    return S[x2][y2] - S[x1 - 1][y2] - S[x2][y1 - 1] + S[x1 - 1][y1 - 1]

# 5. 중심 좌표와 반경에 대한 합 계산 함수
def calculate_area_sum(S, maps, cx, cy, k):
    if k == 0:
        return maps[cx][cy]
    # 십자 모양의 합 계산 (수직 + 수평)
    cross_sum = (
        get_sum(S, cx - k, cy, cx + k, cy) +  # 수직 방향 합
        get_sum(S, cx, cy - k, cx, cy + k) -  # 수평 방향 합
        maps[cx][cy]  # 중심 좌표 중복 제거
    )

    # 정사각형 모양의 합 계산
    square_sum = get_sum(S, cx - (k - 1), cy - (k - 1), cx + (k - 1), cy + (k - 1))

    # 십자 모양의 내부 중복 합 제거
    corrected_cross_sum = (
        get_sum(S, cx - (k - 1), cy, cx + (k - 1), cy) +
        get_sum(S, cx, cy - (k - 1), cx, cy + (k - 1)) -
        maps[cx][cy]
    )

    # 최종 결과 반환
    return cross_sum + square_sum - corrected_cross_sum


ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, calculate_area_sum(S, maps, i, j, K))
    
print(ans)