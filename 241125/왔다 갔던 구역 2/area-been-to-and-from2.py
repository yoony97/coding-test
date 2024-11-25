n = int(input())

current = 0
li = []
offset = 0

# 입력 처리 및 offset 계산
for _ in range(n):
    x, direct = input().split()
    x = int(x)
    li.append((x, direct))
    if direct == 'L':
        x = -x
    current += x
    offset = min(current, offset)

# 최소 offset 기준으로 배열 크기 조정
offset = abs(offset)
ans_size = offset + sum(x for x, d in li if d == 'R') + 1
ans = [0] * ans_size

# Reset current position
current = offset

# Populate ans array
for x, direct in li:
    if direct == 'R':
        for i in range(current, current + x):
            ans[i] += 1
        current += x
    else:
        for i in range(current - 1, current - x - 1, -1):  # Adjusted to avoid overlap
            ans[i] += 1
        current -= x

# Count overlapping segments
cnt = sum(1 for i in ans if i >= 2)
print(cnt)