# 입력 처리
N, Q = map(int, input().split())
li = list(map(int, input().split()))

# 최대 길이 계산 및 리스트 초기화
max_length = max(li)
lines = [0] * (max_length + 1)  # 최대 길이 +1로 안전하게 설정
S = [0] * (max_length + 2)  # Prefix sum 배열도 +2로 설정

# 해당 길이의 라인 표시
for i in li:
    lines[i] = 1  # 1로 표시 (0 기반에서 i-1이 필요 없음)

# Prefix sum 배열 계산
for i in range(1, max_length + 1):
    S[i] = S[i - 1] + lines[i]

# 구간 합 계산 함수
def get_sum(s, e):
    return S[e] - S[s - 1]

# 쿼리 처리
for _ in range(Q):
    s, e = map(int, input().split())  # 1 기반 입력
    if 1 <= s <= max_length and 1 <= e <= max_length:  # 1 기반 경계 조건
        print(get_sum(s, e))
    else:
        print(0)