n = int(input())
numbers = [int(input()) for _ in range(n)]

# Step 1: 누적합 및 나머지 계산
psum = [0] * (n+1)
for i in range(n):
    psum[i+1] = psum[i] + numbers[i]

# Step 2: 나머지 값의 첫 등장 및 마지막 등장 위치 저장
first_seen = {}  # psum[i] % 7 -> 처음 등장한 index
max_range = 0

for i in range(n+1):
    mod = psum[i] % 7  # 누적합을 7로 나눈 나머지
    
    if mod not in first_seen:
        first_seen[mod] = i  # 첫 등장 인덱스 저장
    else:
        # 같은 나머지를 가진 가장 먼 위치의 차이를 구함
        max_range = max(max_range, i - first_seen[mod])

print(max_range)