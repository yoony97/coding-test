def get_sum(S, s, e):
    return S[e] - S[s - 1]

def preprocess(numbers):
    n = len(numbers)
    prefix = [0] * (n + 1)  # prefix[i]는 numbers[0]부터 numbers[i-1]까지의 0이 아닌 수 개수
    for i in range(n):
        prefix[i + 1] = prefix[i] + (1 if numbers[i] != 0 else 0)
    return prefix

N, K, B = map(int, input().split())
original = list(range(1, N + 1))
onumbers = [1] * N  # 1로 초기화, 고장난 신호등은 0으로 변경
bnumbers = [0] * N  # 고장난 신호등을 기록

for _ in range(B):
    blank = int(input())
    onumbers[blank - 1] = 0  # 해당 위치의 신호등이 고장남
    bnumbers[blank - 1] = 1  # 고장난 신호등 위치 표시

# 고장난 신호등의 누적 합 (Prefix Sum)
counting = preprocess(bnumbers)

# 슬라이딩 윈도우를 사용해 최소 고장난 신호등 개수 찾기
answer = float('inf')
for i in range(1, N - K + 2):
    broken_in_range = get_sum(counting, i, i + K - 1)
    answer = min(answer, broken_in_range)

print(answer)